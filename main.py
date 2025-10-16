import streamlit as st

def get_purchase_code():
    st.title("Purchase Category Code Helper")

    part = st.radio("Is this for a part?", ["Yes", "No"])

    if part == "Yes":
        part_type = st.selectbox("Select the type:", ["Non-billable", "Billable", "Contracted"])
        return {"Non-billable": "Parts: Non-Billable (Internal) 60082A", "Billable": "Parts: Billable 60081", "Contracted": "Parts: Contracted 60082B"}[part_type]

    else:
        vendor_supply = st.radio("Is this for a vendor repair?", ["Yes", "No"])

        if vendor_supply == "Yes":
            vendor_type = st.selectbox("Is this billable or non-billable?", ["Billable", "Non-billable"])
            return {"Billable": "Vendor Repairs: Billable 63122", "Non-billable": "Vendor Repairs: Non-Billable 63123"}[vendor_type]

        else:
            biomed_equip = st.radio("Is this for biomed equipment?", ["Yes", "No"])

            if biomed_equip == "Yes":
                biomed_type = st.selectbox("Type of biomed equipment:", ["<$5000", ">$5000", "Furniture<$5000"])
                return {"<$5000": "Equipment <$5000 65002", ">$5000": "Equipment >$5000 65007", "Furniture<$5000": "Equipment: Furniture <$5000 65051"}[biomed_type]

            else:
                misc_equip = st.radio("Is this for certifications, awards, or subscriptions?", ["Yes", "No"])

                if misc_equip == "Yes":
                    misc_type = st.selectbox("Select the type:", ["Certification", "Award", "Membership sub", "Magazine sub"])
                    return {
                        "Certification": "Certification: Tests and Renewals 64039",
                        "Award": "Sponsored Award 84000",
                        "Membership sub": "Subscription: Memberships 60561",
                        "Magazine sub": "Subscription: Magazines 60163"
                    }[misc_type]

                else:
                    gen_equip = st.radio("Is this for general supplies?", ["Yes", "No"])

                    if gen_equip == "Yes":
                        gen_type = st.selectbox("Select the supply type:", [
                            "Book", "Office staples", "Shipping", "Vehicle maintenance", "Consumables", "Computing"
                        ])
                        return {
                            "Book": "Books 60161",
                            "Office staples": "Supplies: Office Staples 60001",
                            "Shipping": "Supplies: Shipping 60123",
                            "Vehicle maintenance": "Supplies: Vehicle Maintence 63128",
                            "Consumables": "Supplies: Technician Consumables 63127",
                            "Computing": "Supplies: Computing 60005"
                        }[gen_type]
                    else:
                        st.error("No matching category found.")
                        return None

# Main logic
code = get_purchase_code()
if code:
    st.success(f"Suggested Purchase Code: **{code}**")