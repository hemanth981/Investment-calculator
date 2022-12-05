import locale
import random
class COL:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    purple = '\033[95m'
    cyan = '\033[96m'
    bright = '\033[97m'
    default = '\033[0m'
locale.setlocale(locale.LC_MONETARY, 'en_IN')
def calculate(initial_amt = 0, sip_amt = 0, num_years = 10, interest = 10.0):
    total_interest = 0
    if type(interest) == list:
        interest_is_random = True
        print((COL.red + "{:<6}" + COL.green + "{:<20}" + COL.default + "{:<20}" + COL.purple + "{:20}" + COL.bright + "{:<20}" + COL.yellow + "{:<20}" + COL.cyan + "{:<20}").format("Year", "Starting Amt", "SIP Amt", "Interest", "Interest calc on", "Interest amt", "Year end amt"))
    else:
        interest_is_random = False
        print((COL.red + "{:<6}" + COL.green + "{:<20}" + COL.default + "{:<20}" + COL.purple + "{:20}" + COL.yellow + "{:<20}" + COL.cyan + "{:<20}").format("Year", "Starting Amt", "SIP Amt", "Interest calc on", "Interest amt", "Year end amt"))
    yearly_amt = sip_amt * 12
    investment = initial_amt
    for i in range(num_years):
        if interest_is_random:
            interest_rate_used = float(random.randrange(int(min(interest)*100), int(max(interest)*100)) / 100.0)
        else:
            interest_rate_used = interest

        year_start_amt = investment
        interest_calc_on = year_start_amt + yearly_amt
        interest_amt = float(interest_rate_used/100.0) * interest_calc_on
        total_interest += interest_amt
        investment = year_start_amt + yearly_amt + interest_amt
        print("\033[0m---------------------------------------------------------------------------------------------------------------------------------------------------------")
        if interest_is_random:
            print((COL.red + "{:<6}" + COL.green + "{:<20}" + COL.default + "{:<20}" + COL.purple + "{:<20}" + COL.bright + "{:<20}" + COL.yellow + "{:<20}" + COL.cyan + "{:<20}").format(i+1, locale.currency(year_start_amt, grouping=True), locale.currency(yearly_amt, grouping=True), locale.currency(interest_calc_on, grouping=True), interest_rate_used, locale.currency(interest_amt, grouping=True), locale.currency(investment, grouping=True)))
        else:
            print((COL.red + "{:<6}" + COL.green + "{:<20}" + COL.default + "{:<20}" + COL.purple + "{:<20}" + COL.yellow + "{:<20}" + COL.cyan + "{:<20}").format(i+1, locale.currency(year_start_amt, grouping=True), locale.currency(yearly_amt, grouping=True), locale.currency(interest_calc_on, grouping=True), locale.currency(interest_amt, grouping=True), locale.currency(investment, grouping=True)))

    total_investment = initial_amt + (sip_amt * 12 * num_years)
    print("\033[0m---------------------------------------------------------------------------------------------------------------------------------------------------------")
    if interest_is_random:
        print(COL.blue + "{:<6}{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("FINAL", "", locale.currency(total_investment, grouping=True), "", "", locale.currency(total_interest, grouping=True), locale.currency(investment, grouping=True)))
    else:
        print(COL.blue + "{:<6}{:<20}{:<20}{:<20}{:<20}{:<20}".format("FINAL", "", locale.currency(total_investment, grouping=True), "", locale.currency(total_interest, grouping=True), locale.currency(investment, grouping=True)))
    print(COL.default)
    if investment == 0:
        print("Nothing invested, 0 gains")
        return
    print("==================================================")
    print("#                     STATS                      #")
    print("==================================================")
    print((COL.default + "#   {:<21}" + COL.blue + "{:>21}   " + COL.default + "#").format("Initial investment", locale.currency(initial_amt, grouping=True)))
    print((COL.default + "#   {:<21}" + COL.blue + "{:>21}   " + COL.default + "#").format("Interest rate", str(interest)))
    print((COL.default + "#   {:<21}" + COL.blue + "{:>21}   " + COL.default + "#").format("Monthly SIP amount", locale.currency(sip_amt, grouping=True)))
    print((COL.default + "#   {:<21}" + COL.blue + "{:>21}   " + COL.default + "#").format("Yearly SIP amount", locale.currency(yearly_amt, grouping=True)))
    print("--------------------------------------------------")
    print((COL.default + "#   {:<21}" + COL.blue + "{:>21}   " + COL.default + "#").format("Total Investment", locale.currency(total_investment, grouping=True)))
    print((COL.default + "#   {:<21}" + COL.blue + "{:>21}   " + COL.default + "#").format("Total interest earned", locale.currency(total_interest, grouping=True)))
    print((COL.default + "#   {:<21}" + COL.blue + "{:>21}   " + COL.default + "#").format("Total value", locale.currency(investment, grouping=True)))
    print((COL.default + "#   {:<21}" + COL.blue + "{:>19.2f} %   " + COL.default + "#").format("% investment", (float(total_investment)/investment) * 100.0))
    print((COL.default + "#   {:<21}" + COL.blue + "{:>19.2f} %   " + COL.default + "#").format("% gained as interest", (float(total_interest)/investment) * 100.0))
    print("==================================================")

if __name__ == '__main__':
    initial_amt = float(input("Initial investment amount: "))
    monthly_sip_amt = float(input("Monthly SIP amount: "))
    num_years = int(input("Number of years: "))
    expected_interest = input("Expected avg interest rate: ").split(',')
    expected_interest = [float(i) for i in expected_interest]
    if len(expected_interest) == 1:
        expected_interest = expected_interest[0]
    calculate(initial_amt = initial_amt, sip_amt = monthly_sip_amt, num_years = num_years, interest = expected_interest)
