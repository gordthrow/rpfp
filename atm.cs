using System;
using System.Collections.Generic;

namespace ATM
{
    class Program
    {
        static void Main(string[] args)
        {
            string cardNumber = "1234567890"; 
            int pin = 1234; 
            int maxWithdrawalAmount = 1000;
            int maxTransactionsPerDay = 10;
            int totalTransactionsToday = 0;
            List<string> transactions = new List<string>();

            Console.WriteLine("Welcome to the ATM");

            // Input card number
            Console.Write("Please enter your card number: ");
            string inputCardNumber = Console.ReadLine();

            // Verify card number
            if (inputCardNumber != cardNumber)
            {
                Console.WriteLine("Invalid card number");
                return;
            }

            // Input PIN
            Console.Write("Please enter your PIN: ");
            int inputPin = Convert.ToInt32(Console.ReadLine());

            // Verify PIN
            if (inputPin != pin)
            {
                Console.WriteLine("Invalid PIN");
                return;
            }

            // Show options
            Console.WriteLine("1. Check cash availability");
            Console.WriteLine("2. View previous five transactions");
            Console.WriteLine("3. Withdraw cash");

            // Input option
            Console.Write("Please select an option: ");
            int option = Convert.ToInt32(Console.ReadLine());

            switch (option)
            {
                case 1:
                    Console.WriteLine("Cash available: $1000");
                    break;
                case 2:
                    Console.WriteLine("Previous transactions:");
                    if (transactions.Count == 0)
                    {
                        Console.WriteLine("No transactions found");
                    }
                    else
                    {
                        for (int i = Math.Max(0, transactions.Count - 5); i < transactions.Count; i++)
                        {
                            Console.WriteLine(transactions[i]);
                        }
                    }
                    break;
                case 3:
                    // Input withdrawal amount
                    Console.Write("Please enter withdrawal amount (up to $1000): ");
                    int withdrawalAmount = Convert.ToInt32(Console.ReadLine());

                    // Verify withdrawal amount
                    if (withdrawalAmount <= 0 || withdrawalAmount > maxWithdrawalAmount)
                    {
                        Console.WriteLine("Invalid withdrawal amount");
                        return;
                    }

                    // Check number of transactions
                    if (totalTransactionsToday >= maxTransactionsPerDay)
                    {
                        Console.WriteLine("Maximum transactions reached for today");
                        return;
                    }

                    // Verify cash availability
                    if (withdrawalAmount > 1000)
                    {
                        Console.WriteLine("Insufficient funds");
                        return;
                    }

                    // Withdraw cash and update transactions
                    Console.WriteLine("Cash withdrawal successful");
                    transactions.Add(string.Format("Withdrawal of ${0} on {1}", withdrawalAmount, DateTime.Now.ToString()));
                    totalTransactionsToday++;
                    break;
                default:
                    Console.WriteLine("Invalid option");
                    break;
            }
        }
    }
}