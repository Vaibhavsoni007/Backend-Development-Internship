import threading
import time


class JobService:

    jobs = {}
    job_counter = 1


    @classmethod
    def start_document_processing(cls, document_id):

        job_id = cls.job_counter
        cls.job_counter += 1


        cls.jobs[job_id] = {
            "document_id": document_id,
            "status": "processing"
        }


        thread = threading.Thread(
            target=cls.process_document,
            args=(job_id,)
        )

        thread.start()


        return job_id


    @classmethod
    def process_document(cls, job_id):

        # Simulate heavy processing
        time.sleep(10)


        cls.jobs[job_id]["status"] = "completed"


    @classmethod
    def get_job_status(cls, job_id):

        return cls.jobs.get(
            job_id,
            {
                "error": "Job not found"
            }
        )