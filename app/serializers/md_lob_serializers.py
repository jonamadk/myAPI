def mdLineOFBusinessEntity(md_line_of_business) -> dict:
    return {
            "_id":md_line_of_business['_id'],
            "code":md_line_of_business['code'],
            "carrierCode":md_line_of_business['carrierCode'],
            "broadLineBusinessCode":md_line_of_business['broadLineBusinessCode'],
            "carrierName":md_line_of_business['carrierName'],
            "carrierWebsite":md_line_of_business['carrierWebsite'],
            "enabled":md_line_of_business['enabled'],
            "_class":md_line_of_business['_class'],
            "carrierLogo":md_line_of_business['carrierLogo'],
            "jurisdictions":md_line_of_business['jurisdictions']
        }