datadict = {"marketing": {"title": ["impressions", "clicks", "visits", "conversions"]
                          },
            "rates": {"title": ["CTR", "CR", "ROI"]},
            "sales": {"title": ["revenue", "purchases", "profit"]},
            "overview": {"title": []}
            }


def cardTitle(dict):
    return dict


def cardSumValue(colName, data):
    return data[colName].sum()


def cardRateValue(colName, divider, data):
    return data[colName].sum() / data[divider].sum()
