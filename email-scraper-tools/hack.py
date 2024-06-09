import webbrowser

company_name = input("Enter the company name: ")

webbrowser.open(f'https://www.linkedin.com/search/results/all/?keywords={company_name}%20university%20recruiter&origin=TYPEAHEAD_HISTORY&searchId=ff55f22e-6d0d-4187-a7e3-86ab0073a40c&sid=Ndw')

name = input("Enter your name: ")
# Text template
template = f"""Hi {name},

I am reaching out to you because I recently applied to the Summer 2024 SWE Intern position at {company_name}, and I believe I have qualifications that might interest you.

I am a student majoring in Electrical & Computer Engineering at the University of Washington @ Seattle. I am familiar with many frontend tech stacks (React, Next, Vue, Tailwind) and machine learning frameworks (Tensorflow, Pytorch, SciKit). You can see examples of my work on my personal portfolio [https://teddygat0r.vercel.app]

Thank you so much for your time and consideration. I’ve also attached my resume if you ever need it!

Thank you,
Joshua Zhang
408-888-8361
"""

t2 = f"Ex. DHS Intern interested in SWE @ {company_name}"

# Print the filled template
print("\n\n")
print(template)
print("\n\n")
print(t2)
print("\n\n")