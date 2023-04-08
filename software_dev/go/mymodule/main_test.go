package main

import "testing"

func TestAdd(t *testing.T) {
	got := Add(8, 4)
	want := 12
	if got != want {
		t.Errorf("Add() = %q, want %q", got, want)
	}
}
