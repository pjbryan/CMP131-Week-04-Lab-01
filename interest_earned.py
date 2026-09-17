# PJ Bryan
# CMP-131-80230
# Week 04
# Lab 01
# Assignment 3
# 09/16/2026

principalAmount = ("Principal Amount: $")
annualInterestRate = ("Annual Interest Rate: %")
divider = "__________________________________"

print("INPUT", divider)
principalAmountInput = float(input(principalAmount))
annualInterestInput = float(input(annualInterestRate))
compoundingPeriods = int(input("Compounding Periods: "))

print()

interestConversion = annualInterestInput / 100
finalAmount = principalAmountInput * (1 + interestConversion / compoundingPeriods) ** compoundingPeriods
interestEarned = finalAmount - principalAmountInput

print("REPORT SUMMARY", divider)
print(f"Principal Amount: ${principalAmountInput:.2f}")
print(f"Annual Interest Rate: {annualInterestInput}%")
print("Compounding Periods:", compoundingPeriods)
print(f"Interest Earned: ${interestEarned:.2f}")
print(f"Final Account Balance: ${finalAmount:.2f}")



