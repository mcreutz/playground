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

type goPackage struct {
	link  string
	stars int
}

func getWebsiteData() *goquery.Document {
	website := "https://www.trackawesomelist.com/avelino/awesome-go/readme/"

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
		link, _ := s.Attr("href")
		text := s.Text()
		if strings.Contains(text, "⭐") {
			startIndex := strings.Index(text, "⭐")
			endIndex := strings.LastIndex(text, ")")
			count := "empty"
			if startIndex != -1 && endIndex != -1 && endIndex > startIndex {
				count = text[startIndex+3 : endIndex]
				if strings.Contains(count, "k") {
					if strings.Contains(count, ".") {
						count = strings.Replace(count, ".", "", 1)
						count = strings.Replace(count, "k", "00", 1)
					} else {
						count = strings.Replace(count, "k", "000", 1)
					}
				}
			}
			countInt, err := strconv.Atoi(count)
			if err != nil {
				fmt.Println(err)
			} else {
				*packages = append(*packages, goPackage{link, countInt})
			}
		}
	})
}

func sortPackages(packages *[]goPackage) {
	// Define a custom sort function based on the values
	sort.Slice(*packages, func(i, j int) bool {
		return *packages[i].stars > *packages[j].stars
	})
}

func printPackages(packages *[]goPackage) {
	// Print first elements of the sorted list
	for i := 0; i < 40; i++ {
		fmt.Printf("%s - %d\n", *packages[i].link, *packages[i].stars)
	}
}

func main() {
	doc := getWebsiteData()
	var packages []goPackage
	var pkgPnt *[]goPackage = &packages
	parsePackageInfo(doc, pkgPnt)
	sortPackages(pkgPnt)
	printPackages(pkgPnt)
}
