package main

import (
	"errors"
	"fmt"
	"log"
)

var (
	ErrInsufficientBalance = errors.New("insufficient balance")
	ErrOverdraftIncurred   = errors.New("overdraft incurred")
)

type Depositable interface {
	Deposit(float64)
}

type Withdrawable interface {
	Withdraw(float64) (float64, error)
}

type BankAccount struct {
	// type can be used as a class replacement, but types hold only data, no bahavior
	// struct is a structure of types
	Owner   string
	balance float64
}

func (ba BankAccount) CheckBalance() float64 {
	// methods are functions, bound to a type
	return ba.balance
}

func (ba *BankAccount) Deposit(amount float64) {
	// type instance can be given as value (variable) or as reference (pointer reference)
	// method's type instances are called receivers
	ba.balance += amount
}

func (ba *BankAccount) Withdraw(amount float64) (float64, error) {
	// additionally to the return-value, an error can be returned
	if ba.balance < amount {
		return 0, ErrInsufficientBalance
	}
	ba.balance -= amount
	return ba.balance, nil
}

type OverdraftableBankAccount struct {
	// There is no inheritance in Go, you need to use composition
	BankAccount
	Fee float64
}

func (oba *OverdraftableBankAccount) Withdraw(amount float64) (float64, error) {
	var err error
	if oba.balance < amount {
		oba.balance -= oba.Fee
		err = ErrOverdraftIncurred
	}
	oba.balance -= amount
	return oba.balance, err
}

func Transfer(debtor Withdrawable, creditor Depositable, amount float64) error {
	balance, err := debtor.Withdraw(amount)
	switch err {
	case ErrInsufficientBalance:
		return err
	case ErrOverdraftIncurred:
		log.Printf("debtor incurred overdraft, new balance is %.2f", balance)
	}
	creditor.Deposit(amount)
	return nil
}

func main() {
	a1 := &BankAccount{"Bob", 50}
	a1.Deposit(20)
	fmt.Println("Balance:", a1.CheckBalance())
	a2 := &OverdraftableBankAccount{BankAccount{"Jill", 100}, 20}
	a2.Deposit(30)
	fmt.Println("Balance for Jill:", a2.CheckBalance())
	_, err := a2.Withdraw(150)
	if err != nil {
		log.Printf("Overdraft incurred: balance is now %2.f", a2.balance)
	}
	_, err = a1.Withdraw(150)
	if err != nil {
		log.Printf("Balance: %2.f", a1.CheckBalance())
	}
	a2.Deposit(100)
	fmt.Println("Account 1 Balance:", a1.CheckBalance(), "Account 2 Balance:", a2.CheckBalance())
	err = Transfer(a1, a2, 100)
	if err != nil {
		log.Printf("Could not complete transfer: %v", err)
	}
	err = Transfer(a2, a1, 100)
	if err != nil {
		log.Printf("Could not complete transfer: %v", err)
	}
	fmt.Println("Account 1 Balance:", a1.CheckBalance(), "Account 2 Balance:", a2.CheckBalance())

}
