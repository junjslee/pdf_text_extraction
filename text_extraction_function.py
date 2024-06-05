# @github.com/junjslee
import requests
import re
import os
from lxml import etree


# @param pdf file you want to extract from
# @function requires GROBID running on local machine (if not, will throw HTTP request error)
# to run local GROBID server: cd grobid --> ./gradlew run
# @return text in a single array
def extract_text_from_pdf(pdf_path):
    # input validation
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError("PDF file not found.")
    
    # GROBID service URL
    grobid_url = 'http://localhost:8070/api/processFulltextDocument'

    # Additional GROBID parameters
    params = {
        'consolidate_citations': False,
        'tei_coordinates': False,
        'force': True
    }

    # Send a request to GROBID
    with open(pdf_path, 'rb') as file:
        files = {'input': file}
        response = requests.post(grobid_url, files=files, params=params)        
        text = response.text
        print(text)

        # handle references for tables & figures
        def remove_ref_tags(text):
            # Define the regular expression pattern to match <ref> tags and their contents
            pattern = r"<ref.*?>(.*?)</ref>"

            def replace(match):
                return match.group(1)

            # Use the re.sub() function to replace all occurrences of the pattern with an empty string
            cleaned_text = re.sub(pattern, replace, text)

            return cleaned_text
        modified_text = remove_ref_tags(text)
        # print(modified_text)


        # handle HTTP link
        def remove_http_links(text):
            # Define the regular expression pattern to match HTTP links
            pattern = r'https?://\S+'
    
            # Use the re.sub() function to replace all occurrences of the pattern with an empty string
            cleaned_text = re.sub(pattern, "", text)
    
            return cleaned_text

        # Define a function to extract content from a <div> element
        def extract_content_from_div(div):
            content = ''
            for element in div.iterchildren():
                if element.tag == "{http://www.tei-c.org/ns/1.0}head":
                    content += f"\n {element.text.strip()}"
                elif element.tag == "{http://www.tei-c.org/ns/1.0}p":
                    content += f"\n{element.text.strip()}"
            return content.strip()

        # raw text extraction from TEI-XML
        root = etree.fromstring(modified_text.encode())

        # Extract content from each <div> element in the <body>
        content_sections = []
        for div in root.xpath("//tei:div", namespaces={"tei": "http://www.tei-c.org/ns/1.0"}):
            content_sections.append(extract_content_from_div(div))

        # Join the content sections into a single string
        final_content = "\n".join(content_sections)
        final_content = remove_http_links(final_content)

    return final_content
        

        
