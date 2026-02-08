"""
Converts US / UK stitch terms into the desired output.
"""
from definitions.stitch_definitions import stitch_definitions


def convert_stitch_term(stitch: str,
                        country: str = None):
    """
    Converts the desired stitch description from one country's terms to another.
    
    :param stitch: the stitch to convert.
    :param country: country to convert from.
    :returns: the stitch description of the other country.
    """
    # if country == "us":
    #     other_country = "uk"
    # else:
    #     other_country = "us"

    st = stitch_definitions[stitch]
    print(st.uk)
    print(st.us)
    print(st.definition)

convert_stitch_term("double_crochet")