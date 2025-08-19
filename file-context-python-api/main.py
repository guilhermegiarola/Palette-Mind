#!/usr/bin/env python3
"""
Main entry point for the Flask application.
This allows us to use relative imports properly.
"""

from controller.api_controller import app

if __name__ == '__main__':
    app.run(debug=True)

