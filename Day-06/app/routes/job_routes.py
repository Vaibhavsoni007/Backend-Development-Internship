from flask import jsonify
from app.services.job_service import JobService


def register_job_routes(app):

    @app.route("/process-document/<int:document_id>", methods=["POST"])
    def process_document(document_id):

        job_id = JobService.start_document_processing(
            document_id
        )

        return jsonify({
            "message": "Document processing started",
            "job_id": job_id,
            "status": "processing"
        }), 202


    @app.route("/job-status/<int:job_id>", methods=["GET"])
    def get_job_status(job_id):

        status = JobService.get_job_status(job_id)

        return jsonify(status), 200