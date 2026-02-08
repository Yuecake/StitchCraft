"""
Docstring for stitch_definitions
"""

from dataclasses import dataclass

@dataclass
class Stitch:
    uk: str             # UK abbreviation
    us: str             # US abbreviation
    definition: str     # English description

stitch_definitions = {
    "slip_stitch": Stitch(
        uk="sl st",
        us="sl st",
        definition="Pull up a loop, then pull that same loop through the working loop."
    ),
    "single_crochet": Stitch(
        uk="dc",
        us="sc",
        definition="The basic crochet stitch: insert hook, yarn over, pull up a loop, yarn over, pull through both loops."
    ),
    "double_crochet": Stitch(
        uk="tr",
        us="dc",
        definition="Yarn over, insert hook, pull up a loop, yarn over, pull through two loops, then two loops again."
    ),
    "half_double_crochet": Stitch(
        uk="htr",
        us="hdc",
        definition="Yarn over, insert hook, pull up a loop, yarn over, pull through all loops."
    ),
    "double_treble_crochet": Stitch(
        uk="dtr",
        us="tr",
        definition="Yarn over twice, insert the hook into the stitch, yarn over and pull up a loop. Yarn over and pull through two loops at a time three times until only one loop remains on the hook."
    ),
    "triple_treble_crochet": Stitch(
        uk="trtr",
        us="dtr",
        definition="A tall, open stitch created by wrapping the yarn around the hook twice before inserting it into a stitch, then working off two loops three separate times."
    ),
    "raised_treble_front": Stitch(
        uk="RtrF",
        us="fpdc",
        definition=""
    ),
    "raised_treble_back": Stitch(
        uk="RtrB",
        us="bpdc",
        definition=""
    ),
    "yarn_over_hook": Stitch(
        uk="yoh",
        us="yo",
        definition=""
    )
}