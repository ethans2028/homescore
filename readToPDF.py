from fpdf import FPDF
import os

# Define a custom PDF class with a header and footer
class PDF(FPDF):
    def header(self):
        # Add an image to the header; adjust the path as necessary
        self.image('homescoreLogo.png', 10, 8, 85)
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, '', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
   
# Function to create a PDF in the specified directory with a specified filename
def create_pdf(directory, filename):
    pdf = PDF()

    # Set font
    pdf.set_font("Times", size=12)

    # Gets width and height
    page_width = pdf.w  # Full page width
    page_height = pdf.h  # Full page height

    # Set fill color to light blue for the right half of the page
    pdf.set_fill_color(160, 223, 240)  # RGB for light blue

    # Define cell dimensions
    cell_height = (pdf.h - 2 * pdf.t_margin) / 18  # Height of each cell to make 18 rows

    # Add pages and draw content
    for page in range(2):
        pdf.add_page()

        # Draw a filled rectangle on the right half of the page
        pdf.rect(pdf.w / 2, 0, pdf.w / 2, pdf.h, 'F')

        # Draw the table
        for row in range(17):
            x = pdf.l_margin
            y = pdf.t_margin + row * cell_height
            pdf.set_xy(x, y)
            pdf.cell(pdf.w - 2 * pdf.l_margin, cell_height, border=1)

    # Lazy way of printing out the info page
    pdf.add_page() 
    pdf.cell(200, 10, "**Caveat Emptor**\n", ln=True, align='L')
    pdf.cell(200, 10, "In the realm of real estate, \"caveat emptor,\" or \"buyer beware,\" underscores the buyer's responsibility\n", ln=True, align='L')
    pdf.cell(200, 10, "to thoroughly examine and evaluate a property before committing to purchase. This principle implies\nthat sellers aren't obligated to disclose every detail about the property's condition or potential issues.\nHowever, it's essential to note that legal mandates exist, especially concerning the disclosure\nof material defects that could significantly impact the property's value or safety.", ln=True, align='L')
    pdf.cell(200,10, "\n", ln=True, align='L')
    pdf.cell(200, 10, "**Square Footage Discrepancy:**\n", ln=True, align='L')
    pdf.cell(200, 10, "It's imperative to verify the actual finished square footage of a property, especially if disparities exist\nbetween the data provided by the Northwest Multiple Listing Service (NWMLS) and public records.\nFinished square footage encompasses elements such as flooring, walls, ceiling, and heating provisions,\nand any inconsistencies should be addressed to gain clarity on the property's specifications.\n", ln=True, align='L')
    pdf.cell(200,10, "\n", ln=True, align='L')
    pdf.cell(200,10, "**Inaccurate Property Type**\n", ln=True, align='L')
    pdf.cell(200,10, "Instances where additional living spaces have been incorporated into a property, contrary to its listed\nclassification as a single-family residence, may indicate discrepancies in zoning or permitting. This\nunderscores the importance of investigating any potential zoning issues and ensuring compliance with\nrelevant regulations.\n", ln=True, align='L')
    pdf.cell(200,10, "\n", ln=True, align='L')
    pdf.cell(200,10, "**Radiant Heat**\n", ln=True, align='L')
    pdf.cell(200,10, "Radiant heating systems offer an efficient and comfortable means of warming indoor spaces by\nemanating heat directly from surfaces such as floors, walls, or ceilings. Variants like Radiant Floor, Wall,\nand Ceiling Heating each present distinct advantages, including enhanced energy efficiency and\nuniform heat distribution, making them noteworthy options for homeowners seeking effective heating\nsolutions.\n", ln=True, align='L')
    pdf.cell(200,10, "**Heating/Cooling: Mini-Split**\n", ln=True, align='L')
    pdf.cell(200,10, "Mini-split systems represent a versatile and energy-efficient heating, ventilation, and air conditioning\n(HVAC) solution, particularly for homes lacking traditional ductwork. With the ability to provide both\nheating and cooling functions and offering zoning capabilities for personalized comfort, these systems\nrequire professional installation and regular maintenance to optimize performance. Despite potentially\nhigher upfront costs, the advantages of compact size, quiet operation, and potential energy savings\nmake mini-splits an attractive option for homeowners seeking adaptable climate control solutions.\n", ln=True, align='L')
    pdf.cell(200,10, "\n", ln=True, align='L')
    pdf.cell(200,10, "**High Probability of a Flip:**\n", ln=True, align='L')
    pdf.cell(200,10, "Properties bought and sold swiftly often signal \"flips,\" where investors acquire distressed properties,\nrenovate them, and aim to sell them for a profit. To navigate such situations effectively, it's advisable to\nprioritize comprehensive home inspections, conduct thorough investigations, and meticulously\ndocument any work completed and permits obtained. Moreover, the involvement of a seller operating\nas a limited liability company (LLC) might heighten the likelihood of the property being a flip.\n", ln=True, align='L')
    pdf.cell(200,10, "\n", ln=True, align='L')
    pdf.cell(200, 10, "Permit History:\n", ln=True, align='L')

    pdf.add_page()
    pdf.cell(200,10, "\n", ln=True, align='L')
    pdf.cell(200,10, "**Home Went Pending Inspection and Back to Active:**\n", ln=True, align='L')
    pdf.cell(200,10, "The return of a property to the market after being under contract, particularly following an inspection,\nwarrants additional scrutiny. It's prudent to delve deeper into the circumstances surrounding the\nprevious buyer's withdrawal and to conduct an independent inspection to ensure transparency and\nascertain the property's condition.\n", ln=True, align='L')

    pdf.cell(200,10, "\n", ln=True, align='L')
    pdf.cell(200,10, "*FIRPTA\n", ln=True, align='L')
    pdf.cell(200,10, "FIRPTA stands for the Foreign Investment in Real Property Tax Act. It primarily affects buyers in real\nestate transactions involving foreign sellers. If the seller is subject to FIRPTA, it means that when they\nsell real property in the United States, the buyer is required to withhold a portion of the sales proceeds\n(usually 15% of the gross sales price) and remit it to the IRS.\nThe purpose of FIRPTA is to ensure that foreign sellers pay taxes on any gains they make from the sale\nof U.S. real estate. Buyers must withhold this amount as a security against potential tax liabilities that\nthe foreign seller might have. This withholding is done at the time of sale and is separate from any other\ntaxes or fees associated with the transaction.\nBuyers need to be aware of FIRPTA requirements because failure to withhold and remit the required\namount can lead to penalties for the buyer. Additionally, buyers should consult with tax professionals\nor legal advisors to ensure compliance with FIRPTA regulations and to understand any exemptions or\nreduced withholding rates that may apply in specific situations.\n", ln=True, align='L')

    pdf.cell(200,10, "\n", ln=True, align='L')
    pdf.cell(200,10, "**Homeowner Association (HOA):**\n", ln=True, align='L')
    pdf.cell(200,10, "In communities governed by homeowner associations (HOAs), adherence to established rules and\nregulations is paramount. Prospective property buyers should thoroughly assess various aspects,\nincluding HOA fees, rules and regulations, reserve funds, financial stability, amenities, governing\ndocuments, management effectiveness, and any age restrictions that may be in place. This\ncomprehensive evaluation ensures alignment with individual preferences and a clear understanding of\nthe community's dynamics before making a commitment.\n", ln=True, align='L')

    # Check to see if the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create the full path
    file_path = os.path.join(directory, filename)

    # Save the PDF with the full path
    pdf.output(file_path)


# Define the directory and filename
directory = "C:/Users/sachi/Desktop/pandasApp"
filename = "Newexample.pdf"

# Create the PDF
create_pdf(directory, filename)

# Data
'''



  "permitnum": "",
  "permitclass": "Multifamily",
  "permitclassmapped": "Residential",
  "permittypemapped": "Building",
  "permittypedesc": "New",
  "description": "Complete and final...",
  "estprojectcost": "57035.0000",
  "applieddate": "2024-05-10T00:00:00.000",
  "issueddate": "2024-05-10T00:00:00.000",
  "expiresdate": "2025-11-10T00:00:00.000",
  "statuscurrent": "Issued",
  "originaladdress1": "",
  "originalcity": "",
  "originalstate": "",
  "originalzip": "",
  "link": {
    "url": ""
  },
  "latitude": "",
  "longitude": "",
  "location1": {
    "latitude": "",
    "longitude": ""
'''