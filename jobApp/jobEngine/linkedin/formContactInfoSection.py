from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import csv
import time
from ..user.candidateProfile import CandidateProfile
from collections.abc import Iterable
from .linkedinFormBaseElemFinder import LinkedinFormBaseFinder
''' handle linkedin easy apply form Contact info'''

class FormContactInfoHandler():
    def __init__(self) -> None:
        pass

    def _fill_contact_info(self, form: WebElement):
        #self._find_application_form()  # try to find the form
        try:
            divs = self._find_divs_selection_grouping()
            if len(divs) != 0:
                # create the key,value pair for each element on the form
                self._createDictFromFormDiv(divs)
                # fill the form with candidate data
                self._send_user_contact_infos(self.candidate, self.label_elements_map)
                # click next buttton
                self.label_elements_map.clear()
        except:
            print("no contact infos to fill")

    def _send_user_contact_infos(self, user: CandidateProfile, elements_dict: dict[WebElement]):
        for label, element in elements_dict.items():
            if label == 'First name':
                self.send_value(element, user.firstname)
            elif label == 'Last name':
                self.send_value(element, user.lastname)
            elif 'Phone country code' in label:
                self.select_option(element, user.phone_code)
            elif label == 'Mobile phone number':
                self.send_value(element, user.phone_number)
            elif 'Email address' in label:
                self.select_option(element, user.email)
            else:
                raise ValueError("Unsupported label: {}".format(label))
