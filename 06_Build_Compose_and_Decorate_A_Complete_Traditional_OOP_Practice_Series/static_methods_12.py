# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.



from colorama import init, Fore, Style # type: ignore


init(autoreset=True)


# 🌡️ Main Heading
print(Fore.MAGENTA + Style.BRIGHT + "\n========== 🌡️ TEMPERATURE CONVERTER SYSTEM ==========\n")



class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        f = (c * 9/5) + 32
        return f
    


# Example usage with colorful output
celsius_temp = 37
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)



print(Fore.CYAN + f"🌬️  Celsius Temperature : {celsius_temp}°C")
print(Fore.YELLOW + f"🔥 Fahrenheit Equivalent : {fahrenheit_temp}°F")
