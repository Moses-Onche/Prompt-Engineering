#!/usr/bin/python3
"""Using iterative prompting"""

fact_sheet = f"""
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100) 
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black, 
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
     medium (1.8 lb/ft3) or high (2.8 lb/ft3)
     - Armless or 8 position PU armrests 

     MATERIALS
     SHELL BASE GLIDER
     - Cast Aluminum with modified nylon PA6/PA66 coating.
     - Shell thickness: 10 mm.
     SEAT
     - HD36 foam

     COUNTRY OF ORIGIN
     - Italy
"""
"""
Components of the prompt:
    Clarity through context - aim and objectives
    Specification of task - keywords for expected output
"""

prompt = f"""
Your task is to assist a marketing team to write a product description
for a website using a technical description.

Write a product description using the technical information
delimited by triple backticks.
technical information: ```fact_sheet```
"""
response = get_completion(prompt)
print(response)
