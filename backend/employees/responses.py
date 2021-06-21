from drf_yasg import openapi
from rest_framework import status
from employees.serializer import EmployeeSerializer, EmployeeSkillSerializer

employee_response_list = {
    'employees': {
        status.HTTP_200_OK: openapi.Response(
            description="200: Successfully read list of employees",
            examples={
                "application/json":
                    {'data': [
                        {
                            "id": 0,
                            "firstname": "string",
                            "lastname": "string",
                            "employee_email": "user@example.com"
                        }
                    ]
                    }
            },
            schema=EmployeeSerializer
        )
    },
    'employees_skills': {
        status.HTTP_200_OK: openapi.Response(
            description="200: Successfully read list of employees skills",
            examples={
                "application/json":
                    {'data': [
                        {
                            "employee_id": 0,
                            "firstname": "string",
                            "lastname": "string",
                            "skills": [
                                {
                                    "seniority_level": 0,
                                    "skill_id": 0
                                }
                            ]
                        }
                    ]
                    }
            }
        )
    },
    'employee_skills': {
        status.HTTP_200_OK: openapi.Response(
            description="200: Successfully read list of employees skills",
            examples={
                "application/json":
                    {
                        "employee_id": 0,
                        "firstname": "string",
                        "lastname": "string",
                        "skills": [
                            {
                                "seniority_level": 0,
                                "skill_id": 0
                            },
                        ]
                    }
            }
        )
    },
    'add_employee_skills': {
            status.HTTP_200_OK: openapi.Response(
                description="200: Successfully add skills to employee",
                examples={
                    "application/json":
                        {'Created id': 0}
                }
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                            description="404: Not Found",
                            examples={
                                "application/json":
                                    ['Employee not found',
                                     'Skill not found',
                                     ]
                            }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                                        description="400: Bad Request",
                                        examples={
                                            "application/json":
                                                ['Skill already exists',
                                                 'Incorrect data',
                                                 ]
                                        }
                        )
        },
    'edit_employee_skills': {
                status.HTTP_200_OK: openapi.Response(
                    description="200: Successfully edit employees skill",
                    examples={
                        "application/json":
                            {'Edited id': 0}
                    }
                ),
                status.HTTP_404_NOT_FOUND: openapi.Response(
                                description="404: Not Found",
                                examples={
                                    "application/json":
                                        ['Employee not found',
                                         'Skill not found',
                                         'Employee with current skill_id not found',
                                         ]
                                }
                ),
                status.HTTP_400_BAD_REQUEST: openapi.Response(
                                            description="400: Bad Request",
                                            examples={
                                                "application/json":
                                                    'Incorrect data',

                                            }
                            )
            },
    'delete_employee_skills': {
                    status.HTTP_200_OK: openapi.Response(
                        description="200: Successfully deleted employees skill",
                        examples={
                            "application/json":
                                {'Deleted id': 0}
                        }
                    ),
                    status.HTTP_404_NOT_FOUND: openapi.Response(
                                    description="404: Not Found",
                                    examples={
                                        "application/json":
                                            ['Employee not found',
                                             'Skill not found',
                                             'Employee with current skill_id not found',
                                             ]
                                    }
                    ),
    },
    'employees_weight': {
            status.HTTP_200_OK: openapi.Response(
                description="200: Successfully calculated correspondence of employees skills",
                examples={
                    "application/json":
                        {
                            "id": 0,
                            "name": "string",
                            "skills": [
                                {
                                    "seniority_level": 0,
                                    "skill_id": 0
                                },
                            ]
                        }
                }
            )
        },
}
