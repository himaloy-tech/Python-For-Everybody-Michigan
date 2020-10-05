def computepay(hour, rate):
    # converting hour and rate into a floating point number
    hour = float(hour)
    rate = float(rate)
    if hour < 40:
        total_pay = hour * rate

        return total_pay
    elif hour >=  40:
        extra_hours_worked = hour - 40

        pay_for_40_hours = 40 * rate

        pay_for_extra_hours = extra_hours_worked * 1.5 * rate

        total_pay = pay_for_extra_hours + pay_for_40_hours

        return total_pay

hour = input("Enter the hours worked: ")
rate = input("Enter the rate per hour: ")

print("Pay", computepay(hour, rate))