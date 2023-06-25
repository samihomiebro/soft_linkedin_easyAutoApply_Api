from applicationDirector import ApplicationDirector
from candidateProfile import CandidateProfile

# TODO Move all paths required for a service  to a config file
    
class directApplyMicroService:

    def __init__(self, service_name="direct apply", csv_jobs='jobApp/data/jobs.csv'):
        self.name = service_name
        print(f"initialising {self.name} microservice..")
        candidate = CandidateProfile(resume_path='jobApp/data/zayneb_dhieb_resume_english.pdf', 
                                     firstname="zayneb", lastname="dhieb", 
                                     email= "zaynebdhiab89@gmail.com",   #"dhiebzayneb89@gmail.com", 
                                     phone_number="+21620094923")
        appDirector = ApplicationDirector()
        self.directapp= appDirector.construct_application(candidate_profile=candidate, jobs=csv_jobs, application_type='Direct')

    def run_service(self):
        print(f"running {self.name} microservice..")
        self.directapp.ApplyForAll()

if __name__ == '__main__':
    import sys
    args = sys.argv
    csv_links = ""
    csv_jobs = ""
    # get the csv links
    if args[1] :
        csv_jobs= args[1]
        print(f"csv jobs file: {csv_jobs}")
        jlink = directApplyMicroService(csv_jobs=csv_jobs)
        jlink.run_service()
    else:
        jlink = directApplyMicroService()
        jlink.run_service()