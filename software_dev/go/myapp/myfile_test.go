package main

import "testing"

func TestAdd(t *testing.T) {
	want := 12
	if got := Add(8, 4); got != want {
		t.Errorf("Add() = %q, want %q", got, want)
	}
}
