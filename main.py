import phonenumbers
from phonenumbers import geocoder,carrier,timezone

def validate_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

def get_country_code(phone_number):
    parsed_number = phonenumbers.parse(phone_number)
    return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split()[0]

def perform_phone_number_lookup(phone_number, language):
    parsed_number = phonenumbers.parse(phone_number)
    default_region = phonenumbers.region_code_for_country_code(parsed_number.country_code)
    print("Default region detected:", default_region)
    print("Country code:", get_country_code(phone_number))

    location = geocoder.description_for_number(parsed_number, language)
    print("Geographical Location:", location)

    carrier_info = carrier.name_for_number(parsed_number, language)
    print("Carrier Information:", carrier_info)

def get_timezone(phone_number):
    parsed_number = phonenumbers.parse(phone_number)
    timezone_info = timezone.time_zones_for_number(parsed_number)
    print("Timezone:", timezone_info)

def main():
    while True:
        option = input("Choose an option:\n1. Phone Number Lookup\n2. Get Timezone\nEnter your choice (1/2): ")

        if option == "1":
            phone_number = input("Enter the phone number (including country code): ")
            language = input("Enter language code (e.g., 'en' for English): ")

            if not validate_phone_number(phone_number):
                print("Invalid phone number format. Please enter a valid phone number.")
                continue

            perform_phone_number_lookup(phone_number, language)

        elif option == "2":
            phone_number = input("Enter the phone number (including country code): ")
            get_timezone(phone_number)

        else:
            print("Invalid option. Please enter 1 or 2.")

        choice = input("Do you want to perform another lookup? (yes/no): ").lower()
        if choice != "yes":
            break

if __name__ == "__main__":
    main()
