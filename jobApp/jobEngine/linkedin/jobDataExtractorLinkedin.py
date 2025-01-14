from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import re 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import logging
logger = logging.getLogger(__name__)

class JobDetailsExtractorLinkedin:
    def __init__(self, job:WebElement):
        self.job = job
        self.job_title = None
        self.company = None 
        self.num_applicants = None 
        self.published = None 
        self.job_description = None 
        self.emails = None 
        self.hiring_manager = None 
        self.job_id = None
        self.job_link = None

   ####### use selenium ####
    def getJobLink(self, job: WebElement):
        try:
            link_element: WebElement = WebDriverWait(job, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'a')))
            self.job_link = link_element.get_attribute('href')
            logger.info("extracted job link: %s", self.job_link)
            return self.job_link
        except NoSuchElementException:
            logger.error("job link extraction error")
            raise

    def getJobTitleSelenium(self, job: WebElement):
        #find job title 
        what_data = "job title"
        try:
            self.job_title= job.find_element(By.TAG_NAME, 'a').get_attribute('aria-label')
            logger.info(f"job title: {self.job_title}")
            return self.job_title 
        except:
            logger.info(f"exceptionn occured while extracting job data: {what_data}")

    def getCompanySelenium(self, job: WebElement):
        #find company title 
        what_data = "company name"
        try:
            company=  job.find_element(By.CLASS_NAME,"job-card-container__primary-description ")
            self.company = company.text
            logger.info(f"company: {self.company}")
            return self.company
        except:
            logger.info(f"exceptionn occured while extracting job data: {what_data}")

    def getLocationSelenium(self, job: WebElement):
        #find job title 
        what_data = "location"
        try:
            self.extracted_location = job.find_elements(By.CLASS_NAME, "job-card-container__metadata-item ")[0].text
            # try via html source code: already given in the search bar: skipping here
            logger.info(f"location: {self.extracted_location}")
            return self.extracted_location
        except:
            logger.info(f"exceptionn occured while extracting job data: {what_data}")

    def getNumberApplicants(self, element:WebElement):
        #find job title 
        what_data = "num of applicants"
        try:
            div_element = element.find_element(By.CSS_SELECTOR,'div.job-details-jobs-unified-top-card__primary-description')
            try:
                applicants=  div_element.find_element(By.CSS_SELECTOR,'span.tvm__text--positive')
                self.num_applicants = applicants.text
            except:
                applicants=  div_element.find_elements(By.CSS_SELECTOR,'span.tvm__text--neutral')
                self.num_applicants = applicants[-1].text
            logger.info(f"num_applicants: {self.num_applicants}")
            return self.num_applicants
        except:
            logger.info(f"exceptionn occured while extracting job data: {what_data}")

    def getPublicationDate(self, element:WebElement):
        #find job title 
        what_data = "publication date"
        try:
            self.published  = element.find_elements(By.CLASS_NAME,'job-card-container__footer-item')[0].find_element(By.TAG_NAME, 'time').get_attribute('datetime')
            logger.info(f"published: {self.published}")
            return self.published
        except:
            logger.info(f"exceptionn occured while extracting job data: {what_data}")
    
    def getJobID(self, element:WebElement):
        # extract job id 
        what_data = "job id"
        try:
            # Extract the job ID attribute value
            self.job_id = element.get_attribute('data-occludable-job-id')
            # logger.info the extracted job ID
            logger.info("Job ID: %s", self.job_id)
            return self.job_id
        except:
            logger.info(f"Exceptionn occured while extracting job data: {what_data}")

    def getJobDescriptionText(self, element:WebElement):

        what_data = "job description"
        try:
            # Find the <div> element with the specified class and ID
            div_element = element.find_element(By.CSS_SELECTOR,'div.jobs-description-content__text#job-details')
            # Extract the text content of the <div> element
            content = div_element.text
            # logger.info the extracted content
            self.job_description = "see link directly"
            logger.info(f"Job Details: {self.job_description}")
            #logger.info(content)
            return self.job_description
        except:
            logger.info(f"Exceptionn occured while extracting job data: {what_data}")

    def getCompanyEmails(self, element:WebElement):
        #find job title 
        what_data = "company emails"
        try:
            # Find the <div> element with the specified class and ID
            div_element = element.find_element(By.CSS_SELECTOR,'div.jobs-description-content__text#job-details')
            # Extract the text content of the <div> element
            content = div_element.text
            # Use a regular expression to find email addresses
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            self.emails = re.findall(email_pattern, content)
            # logger.info the extracted email addresses
            logger.info("Extracted Email Addresses:", self.emails)
            return self.emails
        except:
            logger.info(f"exceptionn occured while extracting job data: {what_data}")

    def getHiringManagerName(self, element:WebElement):
        #find job title 
        what_data = "hiring manager"
        try:
            # Find the <span> element with the specified class
            span_element = element.find_element(By.CSS_SELECTOR,'span.jobs-poster__name.t-14.t-black.mb0')
            # Extract the text content of the <span> element
            self.hiring_manager = span_element.text.strip()
            # logger.info the extracted job poster's name
            logger.info("Job Poster's Name: %s", self.hiring_manager)
            return self.hiring_manager
        except:
            logger.info(f"exceptionn occured while extracting job data: {what_data}")
            return None
