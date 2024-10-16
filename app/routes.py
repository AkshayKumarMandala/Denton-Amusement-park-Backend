from flask import request, jsonify
from app.models import User, Service, Feedback, Visitor, Ride, RestArea, AssistiveTechnology, Transportation, ServiceAnimalFacility
from app import db

def setup_routes(app):
    # Route for adding initial services
    @app.route('/api/add_initial_services', methods=['GET'])
    def add_initial_services():
        services = [
            {'name': 'Wheelchair-Friendly Pathways', 'description': 'Accessible paths throughout the park for wheelchair users.'},
            {'name': 'Sensory-Friendly Zones', 'description': 'Quiet and comfortable areas for visitors with sensory sensitivities.'},
            {'name': 'Inclusive Rides', 'description': 'Fun rides that accommodate visitors with different abilities.'},
            {'name': 'Assistive Technologies', 'description': 'Technology support such as audio assistance and visual guides.'}
        ]
        
        for service_data in services:
            service = Service(name=service_data['name'], description=service_data['description'])
            db.session.add(service)
        
        db.session.commit()
        
        return jsonify({'message': 'Initial services added successfully!'}), 201

    # Route for getting all services
    @app.route('/api/services', methods=['GET'])
    def get_services():
        services = Service.query.all()
        result = [{'id': service.id, 'name': service.name, 'description': service.description} for service in services]
        return jsonify(result)

    # Route for adding feedback
    @app.route('/api/feedback', methods=['POST'])
    def submit_feedback():
        data = request.get_json()
        user_id = data.get('user_id')
        message = data.get('message')

        feedback = Feedback(user_id=user_id, message=message)
        db.session.add(feedback)
        db.session.commit()

        return jsonify({'message': 'Feedback submitted successfully'}), 201

    # Other routes go here...
