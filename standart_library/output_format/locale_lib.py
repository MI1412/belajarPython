import locale
# NAME
#     locale - Locale support module.
setlocale =locale.setlocale(locale.LC_ALL,"Indonesian_United States.1252")
print(setlocale)
conv = locale.localeconv()
x = 12345,6
format_locale = locale.format_string("%d",x,grouping=True)
print(format_locale)

format_str = locale.format_string("%s%.*f",(conv["currency_symbol"],conv["frac_digits"],x),grouping=True)
print(format_str)