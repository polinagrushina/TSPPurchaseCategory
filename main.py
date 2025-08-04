import streamlit as st

def get_purchase_code():
    st.title("Purchase Category Code Helper")

    part = st.radio("Is this for a part?", ["Yes", "No"])

    if part == "Yes":
        part_type = st.selectbox("Select the type:", ["Non-billable", "Billable", "Contracted"])
        return {"Non-billable": "60082A", "Billable": "60081", "Contracted": "60082B"}[part_type]

    else:
        vendor_supply = st.radio("Is this for a vendor repair?", ["Yes", "No"])

        if vendor_supply == "Yes":
            vendor_type = st.selectbox("Is this billable or non-billable?", ["Billable", "Non-billable"])
            return {"Billable": "63122", "Non-billable": "63123"}[vendor_type]

        else:
            biomed_equip = st.radio("Is this for biomed equipment?", ["Yes", "No"])

            if biomed_equip == "Yes":
                biomed_type = st.selectbox("Type of biomed equipment:", ["Less", "More", "Furniture"])
                return {"Less": "65002", "More": "65007", "Furniture": "65051"}[biomed_type]

            else:
                misc_equip = st.radio("Is this for certifications, awards, or subscriptions?", ["Yes", "No"])

                if misc_equip == "Yes":
                    misc_type = st.selectbox("Select the type:", ["Certification", "Award", "Membership", "Magazine"])
                    return {
                        "Certification": "64039",
                        "Award": "84000",
                        "Membership": "60561",
                        "Magazine": "60163"
                    }[misc_type]

                else:
                    gen_equip = st.radio("Is this for general supplies?", ["Yes", "No"])

                    if gen_equip == "Yes":
                        gen_type = st.selectbox("Select the supply type:", [
                            "Book", "Office staples", "Shipping", "Vehicle maintenance", "Consumables", "Computing"
                        ])
                        return {
                            "Book": "60161",
                            "Office staples": "60001",
                            "Shipping": "60123",
                            "Vehicle maintenance": "63128",
                            "Consumables": "63127",
                            "Computing": "60005"
                        }[gen_type]
                    else:
                        st.error("No matching category found.")
                        return None

# Main logic
code = get_purchase_code()
if code:
    st.success(f"Suggested Purchase Code: **{code}**")