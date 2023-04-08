package main

import (
	"fmt"
	"log"
	"net/http"
	"sort"
	"strconv"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

func main() {
	doc := getWebsiteContent()
	var packages []goPackage
	packagesPt := &packages
	parsePackageInfo(doc, packagesPt)
	sortPackages(packagesPt)
	printPackages(packagesPt)
}

type goPackage struct {
	linkUrl    string
	starsCount int
}

func getWebsiteContent() *goquery.Document {
	const website = "https://www.trackawesomelist.com/avelino/awesome-go/readme/"

	// Request the HTML document
	res, err := http.Get(website)
	if err != nil {
		log.Fatal(err)
	}
	defer res.Body.Close()
	if res.StatusCode != 200 {
		log.Fatalf("status code error: %d %s", res.StatusCode, res.Status)
	}
	// Load the HTML content
	doc, err := goquery.NewDocumentFromReader(res.Body)
	if err != nil {
		log.Fatal(err)
	}
	return doc
}

func parsePackageInfo(doc *goquery.Document, packages *[]goPackage) {
	// Find all links with "⭐" in text
	doc.Find("a").Each(func(i int, s *goquery.Selection) {
		linkUrl, _ := s.Attr("href")
		linkText := s.Text()
		if !strings.Contains(linkText, "⭐") {
			return
		}
		emoji_length := 3
		starIndex := strings.Index(linkText, "⭐")
		closingIndex := strings.LastIndex(linkText, ")")
		if starIndex == -1 || closingIndex == -1 || closingIndex < starIndex {
			return
		}
		starsCountText := linkText[starIndex+emoji_length : closingIndex]
		if strings.Contains(starsCountText, "k") {
			if strings.Contains(starsCountText, ".") {
				starsCountText = strings.Replace(starsCountText, ".", "", 1)
				starsCountText = strings.Replace(starsCountText, "k", "00", 1)
			} else {
				starsCountText = strings.Replace(starsCountText, "k", "000", 1)
			}
		}
		starsCount, err := strconv.Atoi(starsCountText)
		if err != nil {
			fmt.Println(err)
			return
		}
		*packages = append(*packages, goPackage{linkUrl, starsCount})
	})
}

func sortPackages(packages *[]goPackage) {
	// Define a custom sort function based on the values
	sort.Slice(*packages, func(i, j int) bool {
		return (*packages)[i].starsCount > (*packages)[j].starsCount
	})
}

func printPackages(packages *[]goPackage) {
	// Print first elements of the sorted list
	for i := 0; i < 40; i++ {
		fmt.Printf("%s - %d\n", (*packages)[i].linkUrl, (*packages)[i].starsCount)
	}
}

// todo
// - tests
// - comments
// - error handling
// - website caching, 1 day
// - capsulation
// - package categories
// - remove invalid links like to the awesome site itself
// - show package name / link text
