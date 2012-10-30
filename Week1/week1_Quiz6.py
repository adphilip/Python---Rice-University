#The equation FV = PV (1+rate)periods

#The present value (PV) of your money is how much money you have now.
#The future value (FV) of your money is how much money you will have in the future.
#The interest rate per period (rate) is how much interest you earn as a percentage. The period is length of time between interest payments.
#The number of periods (periods) is how many periods in the future this calculation is for.

#Before submitting your answers, test your function on the following. future_value(500, .04, 10, 10) should return 745.317442823934.

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    future_value = present_value * ((1 + rate_per_period)**periods)
    return future_value
	

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

#745.317442823934.
print "$500 at 4% compounded 10/year for 10 years yields $", future_value(500, .04, 10, 10)
