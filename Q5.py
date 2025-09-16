hour = int(input("Enter the hour of the day (0-23): "))

if hour < 0 or hour > 23:
    print("Invalid hour! Please enter a value between 0 and 23.")
elif 0 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 17:
    print("Good Afternoon!")
else:
    print("Good Evening!")
