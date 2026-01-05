from flask import Flask, jsonify
# import sys
# import os

# --- CÁC PHẦN CHƯA DÙNG ĐẾN ĐƯỢC CHUYỂN THÀNH NOTE ---
# from api.swagger import spec
# from entrypoints.controllers.patient_controller import patient_blueprint
# from entrypoints.controllers.clinic_controller import clinic_blueprint
# from entrypoints.controllers.ai_controller import ai_blueprint
# from entrypoints.controllers.report_controller import report_blueprint
# from api.middleware import middleware
# from api.responses import success_response
# from flasgger import Swagger
# from config import SwaggerConfig
# from flask_swagger_ui import get_swaggerui_blueprint
# ----------------------------------------------------

from infrastructure.databases import init_db, init_models 
from config import Config

def create_app():
    app = Flask(__name__)
    
    # 1. Cấu hình Swagger (Tạm đóng)
    # Swagger(app)
    
    # 2. Đăng ký các Blueprint y tế (Tạm đóng vì chưa có code controller)
    # app.register_blueprint(patient_blueprint, url_prefix='/api/v1/patient')
    # app.register_blueprint(clinic_blueprint, url_prefix='/api/v1/clinic')
    # app.register_blueprint(ai_blueprint, url_prefix='/api/v1/ai')
    # app.register_blueprint(report_blueprint, url_prefix='/api/v1/report')

    # 3. Cấu hình Swagger UI (Tạm đóng)
    # SWAGGER_URL = '/docs'
    # API_URL = '/swagger.json'
    # swaggerui_blueprint = get_swaggerui_blueprint(
    #     SWAGGER_URL,
    #     API_URL,
    #     config={'app_name': "Medical AI API"}
    # )
    # app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # 4. Khởi tạo Database và Tạo bảng
    try:
        init_db(app)
        with app.app_context():
            init_models() 
            print(">>> Database initialized and tables created successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")

    # 5. Đăng ký Middleware (Tạm đóng)
    # middleware(app)

    # 6. Quét routes vào Swagger Spec (Tạm đóng)
    # with app.test_request_context():
    #     for rule in app.url_map.iter_rules():
    #         if any(rule.endpoint.startswith(prefix) for prefix in ['patient_blueprint', 'clinic_blueprint', 'ai_blueprint', 'report_blueprint']):
    #             view_func = app.view_functions.get(rule.endpoint)
    #             if view_func:
    #                 spec.path(view=view_func)

    # @app.route("/swagger.json")
    # def swagger_json():
    #     return jsonify(spec.to_dict())

    @app.route("/")
    def index():
        return jsonify({
            "message": "Retinal Health AI API is running (Infrastructure Mode)",
            "database_status": "Tables mapped"
        })

    return app

if __name__ == '__main__':
    app = create_app()
    # Chạy ứng dụng trên cổng 9999
    app.run(host='0.0.0.0', port=9999, debug=True)