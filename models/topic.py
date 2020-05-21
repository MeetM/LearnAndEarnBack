from models import db


class Topic(db.Model):
    __tablename__ = 'topic'

    topic_id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(255), unique=True, nullable=False)
    topic_param = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, topic_name, topic_param):
        self.topic_name = topic_name
        self.topic_param = topic_param

    @classmethod
    def get_topic(cls, topic_id):
        return cls.query.filter_by(topic_id=topic_id).first()

    @classmethod
    def get_all_topics(cls):
        topics = cls.query.all()
        response = []
        for topic in topics:
            response.append(Topic._response_marshall(topic))
        return response

    @staticmethod
    def _response_marshall(topic):
        return {
            "id": topic.topic_id,
            "name": topic.topic_name,
            "topic_param": topic.topic_param
        }