def get_purchase_code():
    print("Is this for a part? (yes/no)")
    part = input().strip().lower()
    
    if part == "yes":
        print("Is this non-billable, billable, or contracted?")
        part_type = input().strip().lower()

        if part_type == "non-billable":
            return "60082A"
        elif part_type == "billable":
            return "60081"
        elif part_type == "contracted":
            return "60082B"
        else:
            return "Error: Invalid part type. Please rerun and enter answers correctlyno."

    else:
        print("Is this for a vendor repair? (yes/no)")
        vendor_supply = input().strip().lower()

        if vendor_supply == "yes":
            print("Is this billable or non-billable?")
            vendor_type = input().strip().lower()

            if vendor_type == "billable":
                return "63122"
            elif vendor_type == "non-billable":
                return "63123"
            else:
                return "Error: Invalid vendor type. Please rerun and enter answers correctly."

        else:
            print("Is this for biomed equipment? (yes/no)")
            biomed_equip = input().strip().lower()

            if biomed_equip == "yes":
                print("Is it less than or equal to, more than, or furniture less than $5000? (less, more, furniture)")
                biomed_type = input().strip().lower()

                if biomed_type == "less":
                    return "65002"
                elif biomed_type == "more":
                    return "65007"
                elif biomed_type == "furniture":
                    return "65051"
                else:
                    return "Error: Invalid biomed type. Please rerun and enter answers correctly."

            else:
                print("Is this for certifications, awards, or subscriptions? (yes/no)")
                misc_equip = input().strip().lower()

                if misc_equip == "yes":
                    print("Is it a certification, sponsored award, subscription for membership, or subscription for magazine? (certif, award, membership, magazine)")
                    misc_type = input().strip().lower()

                    if misc_type == "certif":
                        return "64039"
                    elif misc_type == "award":
                        return "84000"
                    elif misc_type == "membership":
                        return "60561"
                    elif misc_type == "magazine":
                        return "60163"
                    else:
                        return "Error: Invalid certification/subscription type. Please rerun and enter answers correctly."

                else:
                    print("Is this for general supplies? (yes/no)")
                    gen_equip = input().strip().lower()

                    if gen_equip == "yes":
                        print("Is it a book, office staples, shipping, vehicle maintenance, consumables, or computing?")
                        gen_type = input().strip().lower()

                        if gen_type == "book":
                            return "60161"
                        elif gen_type == "office staples":
                            return "60001"
                        elif gen_type == "shipping":
                            return "60123"
                        elif gen_type == "vehicle maintenance":
                            return "63128"
                        elif gen_type == "consumables":
                            return "63127"
                        elif gen_type == "computing":
                            return "60005"
                        else:
                            return "Error: Invalid general supply type. Please rerun and enter answers correctly."
                    else:
                        return "Error: No matching category found. Please rerun and enter answers correctly."

# Run the decision tree
code = get_purchase_code()
print(f"Purchase Code: {code}")