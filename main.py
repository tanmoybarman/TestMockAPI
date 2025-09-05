from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Dict, Any, List, Optional, Union
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI(
    title="Healthcare Mock API Service",
    version="1.0.0",
    description="Mock API service for healthcare endpoints",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Get allowed origins from environment variable or default to '*'
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Healthcare Mock API"}

# Response Models
class MemberResponse(BaseModel):
    members: List[Dict[str, Any]]

class CoverageResponse(BaseModel):
    coverages: List[Dict[str, Any]]

class AccumulatorResponse(BaseModel):
    member: Dict[str, Any]
    planBenefitsAndAccums: List[Dict[str, Any]]

class ErrorResponse(BaseModel):
    text: str

class OperationOutcome(BaseModel):
    issue: List[Dict[str, Any]]

class FailedAccumulatorResponse(BaseModel):
    operationOutcome: OperationOutcome
    member: Dict[str, Any]
    planBenefitsAndAccums: List[Dict[str, Any]]

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Healthcare Mock API Service",
        "version": "1.0.0",
        "endpoints": [
            {"path": "/searchMemberById/m-a", "methods": ["GET"], "description": "Search for member with ID 'm-a'"},
            {"path": "/searchMemberById/m-b-m-n", "methods": ["GET"], "description": "Search for member with ID 'm-b-m-n'"},
            {"path": "/searchMemberById/m-n-a-c", "methods": ["GET"], "description": "Search for member with ID 'm-n-a-c'"},
            {"path": "/searchMemberById/m-e-r", "methods": ["GET"], "description": "Error response for member search"},
            {"path": "/searchCoverageById/c-s", "methods": ["GET"], "description": "Search for coverage with ID 'c-s'"},
            {"path": "/searchCoverageById/c-n-m-id", "methods": ["GET"], "description": "Search for coverage with ID 'c-n-m-id'"},
            {"path": "/searchCoverageById/c-n-a-c", "methods": ["GET"], "description": "Search for coverage with ID 'c-n-a-c'"},
            {"path": "/searchCoverageById/c-e-r", "methods": ["GET"], "description": "Error response for coverage search"},
            {"path": "/searchAccums/acc-succ", "methods": ["GET"], "description": "Search for accumulator with ID 'acc-succ'"},
            {"path": "/searchAccums/acc-rem-amt-miss", "methods": ["GET"], "description": "Search for accumulator with ID 'acc-rem-amt-miss'"},
            {"path": "/searchAccums/acc-f", "methods": ["GET"], "description": "Search for accumulator with ID 'acc-f' (failure case)"}
        ]
    }

# Member Search Endpoints

# Response data
MEMBER_RESPONSE_MA = {
    "members": [
        {
            "subscriberID": "1234567890000",
            "memberId": "00",
            "socialSecurityID": "12345678",
            "accountNumber": "7634526",
            "masterRecordID": "123qwerty",
            "personNumberExtID": "1234567890000TAN",
            "groupNumber": "7634526",
            "memberEffective": {
                "startDate": "2025-08-15",
                "endDate": "3000-12-31",
                "originalEffectiveDate": "2025-08-15"
            },
            "active": True,
            "name": {
                "memberName": {
                    "fullName": "TEST USER",
                    "lastName": "USER",
                    "firstName": "TEST"
                },
                "normalizedName": {
                    "normalizedLastName": "USER",
                    "normalizedFirstName": "TEST"
                }
            },
            "telecom": [
                {
                    "phoneType": "G",
                    "phoneNumber1": "0000000000",
                    "phoneNumber2": "0000000000",
                    "phoneRank": "1"
                }
            ],
            "email": [
                {
                    "email": "TEST@YOPMAIL.com",
                    "emailRank": "1",
                    "emailSourceIndicator": "TEST_SITE",
                    "currentEmailIndicator": "Y"
                }
            ],
            "gender": "female",
            "birthDate": "09-09-26",
            "deceasedDateTime": "9999-12-31",
            "address": [
                {
                    "use": "home",
                    "type": "G",
                    "addressline1": "KOLKATA",
                    "city": "KOLKATA",
                    "district": "090",
                    "state": "WB",
                    "postalCode": "7000001",
                    "period": {
                        "start": "1900-01-01",
                        "end": "9999-12-31"
                    }
                }
            ],
            "multipleBirthInteger": 0,
            "medicarePartAandBEffectiveDate": "1900-01-01",
            "hospiceIndicator": False,
            "ESRDIndicator": False,
            "directPayIndicator": False,
            "sex": "F",
            "medicareDetail": [
                {
                    "coveragePeriod": {
                        "start": "2025-08-15",
                        "end": "3000-12-31"
                    },
                    "eligibilityRelationship": {
                        "memberStatus": "10",
                        "memberStatusDescription": "ACTIVE MEMBER"
                    },
                    "typeOfContract": "101",
                    "typeOfContractDisplay": "Member only"
                }
            ]
        }
    ]
}

MEMBER_RESPONSE_MBMN = {
    "members": [
        {
            "subscriberID": "1234567890000",
            "memberId": "00",
            "socialSecurityID": "12345678",
            "accountNumber": "7634526",
            "personNumberExtID": "1234567890000TAN",
            "groupNumber": "7634526",
            "memberEffective": {
                "startDate": "2025-08-15",
                "endDate": "3000-12-31",
                "originalEffectiveDate": "2025-08-15"
            },
            "active": True,
            "name": {
                "memberName": {
                    "fullName": "TEST USER",
                    "lastName": "USER",
                    "firstName": "TEST"
                },
                "normalizedName": {
                    "normalizedLastName": "USER",
                    "normalizedFirstName": "TEST"
                }
            },
            "telecom": [
                {
                    "phoneType": "G",
                    "phoneNumber1": "0000000000",
                    "phoneNumber2": "0000000000",
                    "phoneRank": "1"
                }
            ],
            "email": [
                {
                    "email": "TEST@YOPMAIL.com",
                    "emailRank": "1",
                    "emailSourceIndicator": "TEST_SITE",
                    "currentEmailIndicator": "Y"
                }
            ],
            "gender": "female",
            "birthDate": "09-09-26",
            "deceasedDateTime": "9999-12-31",
            "address": [
                {
                    "use": "home",
                    "type": "G",
                    "addressline1": "KOLKATA",
                    "city": "KOLKATA",
                    "district": "090",
                    "state": "WB",
                    "postalCode": "7000001",
                    "period": {
                        "start": "1900-01-01",
                        "end": "9999-12-31"
                    }
                }
            ],
            "multipleBirthInteger": 0,
            "medicarePartAandBEffectiveDate": "1900-01-01",
            "hospiceIndicator": False,
            "ESRDIndicator": False,
            "directPayIndicator": False,
            "sex": "F",
            "medicareDetail": [
                {
                    "coveragePeriod": {
                        "start": "2025-08-15",
                        "end": "3000-12-31"
                    },
                    "eligibilityRelationship": {
                        "memberStatus": "10",
                        "memberStatusDescription": "ACTIVE MEMBER"
                    },
                    "typeOfContract": "101",
                    "typeOfContractDisplay": "Member only"
                }
            ]
        }
    ]
}

MEMBER_RESPONSE_MNAC = {
    "members": [
        {
            "subscriberID": "1234567890000",
            "memberId": "00",
            "socialSecurityID": "12345678",
            "accountNumber": "7634526",
            "masterRecordID": "123qwerty",
            "personNumberExtID": "1234567890000TAN",
            "groupNumber": "7634526",
            "memberEffective": {
                "startDate": "2025-08-15",
                "endDate": "2025-09-04",
                "originalEffectiveDate": "2025-08-15"
            },
            "active": True,
            "name": {
                "memberName": {
                    "fullName": "TEST USER",
                    "lastName": "USER",
                    "firstName": "TEST"
                },
                "normalizedName": {
                    "normalizedLastName": "USER",
                    "normalizedFirstName": "TEST"
                }
            },
            "telecom": [
                {
                    "phoneType": "G",
                    "phoneNumber1": "0000000000",
                    "phoneNumber2": "0000000000",
                    "phoneRank": "1"
                }
            ],
            "email": [
                {
                    "email": "TEST@YOPMAIL.com",
                    "emailRank": "1",
                    "emailSourceIndicator": "TEST_SITE",
                    "currentEmailIndicator": "Y"
                }
            ],
            "gender": "female",
            "birthDate": "09-09-26",
            "deceasedDateTime": "9999-12-31",
            "address": [
                {
                    "use": "home",
                    "type": "G",
                    "addressline1": "KOLKATA",
                    "city": "KOLKATA",
                    "district": "090",
                    "state": "WB",
                    "postalCode": "7000001",
                    "period": {
                        "start": "1900-01-01",
                        "end": "9999-12-31"
                    }
                }
            ],
            "multipleBirthInteger": 0,
            "medicarePartAandBEffectiveDate": "1900-01-01",
            "hospiceIndicator": False,
            "ESRDIndicator": False,
            "directPayIndicator": False,
            "sex": "F",
            "medicareDetail": [
                {
                    "coveragePeriod": {
                        "start": "2025-08-15",
                        "end": "3000-12-31"
                    },
                    "eligibilityRelationship": {
                        "memberStatus": "10",
                        "memberStatusDescription": "ACTIVE MEMBER"
                    },
                    "typeOfContract": "101",
                    "typeOfContractDisplay": "Member only"
                }
            ]
        }
    ]
}

# Coverage Search Endpoints

# Response data
COVERAGE_RESPONSE_CS = {
    "coverages": [
        {
            "businessIdentifier": {
                "subscriberID": "123456789",
                "masterRecordID": "qwerty123",
                "personNumberExtID": "123456789JOE",
                "socialSecurityID": "qwerty321"
            },
            "status": "active",
            "type": {
                "code": "M",
                "display": "Medical"
            },
            "groupNumber": "1111111",
            "grpBillingNumber": "0000",
            "originalEffectiveDate": "2025-08-25",
            "prefixSubscriberID": "ABC123456789",
            "planPrefix": "HHV",
            "dependent": "10",
            "relationship": {
                "code": "10",
                "display": "Dependent"
            },
            "eligibilityRelationship": {
                "code": "45",
                "display": "Dependent Child"
            },
            "coveragePeriod": {
                "start": "2025-08-25",
                "end": "3000-12-31"
            },
            "marketSegmentCode": "Commercial",
            "productLevel": [
                {
                    "lineOfBusiness": {
                        "code": "A1",
                        "display": "Medical"
                    },
                    "planName": {
                        "code": "10017",
                        "display": "LIC"
                    },
                    "productCategory": {
                        "code": "3",
                        "display": "Preferred Provider Plan"
                    },
                    "coveragePackageCode": "123456",
                    "Network": {}
                }
            ],
            "nascoEligibility": {}
        },
        {
            "businessIdentifier": {
                "subscriberID": "123456789",
                "masterRecordID": "qwerty123",
                "personNumberExtID": "123456789JOE",
                "socialSecurityID": "qwerty321"
            },
            "status": "active",
            "type": {
                "code": "M",
                "display": "Medical"
            },
            "groupNumber": "1111111",
            "grpBillingNumber": "0000",
            "originalEffectiveDate": "2025-08-25",
            "prefixSubscriberID": "ABC123456789",
            "planPrefix": "HHV",
            "dependent": "10",
            "relationship": {
                "code": "10",
                "display": "Dependent"
            },
            "eligibilityRelationship": {
                "code": "45",
                "display": "Dependent Child"
            },
            "coveragePeriod": {
                "start": "2024-08-25",
                "end": "2025-08-25"
            },
            "marketSegmentCode": "Commercial",
            "productLevel": [
                {
                    "lineOfBusiness": {
                        "code": "A1",
                        "display": "Medical"
                    },
                    "planName": {
                        "code": "10017",
                        "display": "LIC"
                    },
                    "productCategory": {
                        "code": "3",
                        "display": "Preferred Provider Plan"
                    },
                    "coveragePackageCode": "123456",
                    "Network": {}
                }
            ],
            "nascoEligibility": {}
        }
    ]
}

COVERAGE_RESPONSE_CNMID = {
    "coverages": [
        {
            "businessIdentifier": {
                "subscriberID": "123456789",
                "personNumberExtID": "123456789JOE",
                "socialSecurityID": "qwerty321"
            },
            "status": "active",
            "type": {
                "code": "M",
                "display": "Medical"
            },
            "groupNumber": "1111111",
            "grpBillingNumber": "0000",
            "originalEffectiveDate": "2025-08-25",
            "prefixSubscriberID": "ABC123456789",
            "planPrefix": "HHV",
            "dependent": "10",
            "relationship": {
                "code": "10",
                "display": "Dependent"
            },
            "eligibilityRelationship": {
                "code": "45",
                "display": "Dependent Child"
            },
            "coveragePeriod": {
                "start": "2025-08-25",
                "end": "3000-12-31"
            },
            "marketSegmentCode": "Commercial",
            "productLevel": [
                {
                    "lineOfBusiness": {
                        "code": "A1",
                        "display": "Medical"
                    },
                    "planName": {
                        "code": "10017",
                        "display": "LIC"
                    },
                    "productCategory": {
                        "code": "3",
                        "display": "Preferred Provider Plan"
                    },
                    "coveragePackageCode": "123456",
                    "Network": {}
                }
            ],
            "nascoEligibility": {}
        },
        {
            "businessIdentifier": {
                "subscriberID": "123456789",
                "masterRecordID": "qwerty123",
                "personNumberExtID": "123456789JOE",
                "socialSecurityID": "qwerty321"
            },
            "status": "active",
            "type": {
                "code": "M",
                "display": "Medical"
            },
            "groupNumber": "1111111",
            "grpBillingNumber": "0000",
            "originalEffectiveDate": "2025-08-25",
            "prefixSubscriberID": "ABC123456789",
            "planPrefix": "HHV",
            "dependent": "10",
            "relationship": {
                "code": "10",
                "display": "Dependent"
            },
            "eligibilityRelationship": {
                "code": "45",
                "display": "Dependent Child"
            },
            "coveragePeriod": {
                "start": "2024-08-25",
                "end": "2025-08-25"
            },
            "marketSegmentCode": "Commercial",
            "productLevel": [
                {
                    "lineOfBusiness": {
                        "code": "A1",
                        "display": "Medical"
                    },
                    "planName": {
                        "code": "10017",
                        "display": "LIC"
                    },
                    "productCategory": {
                        "code": "3",
                        "display": "Preferred Provider Plan"
                    },
                    "coveragePackageCode": "123456",
                    "Network": {}
                }
            ],
            "nascoEligibility": {}
        }
    ]
}

COVERAGE_RESPONSE_CNAC = {
    "coverages": [
        {
            "businessIdentifier": {
                "subscriberID": "123456789",
                "masterRecordID": "qwerty123",
                "personNumberExtID": "123456789JOE",
                "socialSecurityID": "qwerty321"
            },
            "status": "active",
            "type": {
                "code": "M",
                "display": "Medical"
            },
            "groupNumber": "1111111",
            "grpBillingNumber": "0000",
            "originalEffectiveDate": "2025-08-25",
            "prefixSubscriberID": "ABC123456789",
            "planPrefix": "HHV",
            "dependent": "10",
            "relationship": {
                "code": "10",
                "display": "Dependent"
            },
            "eligibilityRelationship": {
                "code": "45",
                "display": "Dependent Child"
            },
            "coveragePeriod": {
                "start": "2025-08-25",
                "end": "2025-09-04"
            },
            "marketSegmentCode": "Commercial",
            "productLevel": [
                {
                    "lineOfBusiness": {
                        "code": "A1",
                        "display": "Medical"
                    },
                    "planName": {
                        "code": "10017",
                        "display": "LIC"
                    },
                    "productCategory": {
                        "code": "3",
                        "display": "Preferred Provider Plan"
                    },
                    "coveragePackageCode": "123456",
                    "Network": {}
                }
            ],
            "nascoEligibility": {}
        },
        {
            "businessIdentifier": {
                "subscriberID": "123456789",
                "masterRecordID": "qwerty123",
                "personNumberExtID": "123456789JOE",
                "socialSecurityID": "qwerty321"
            },
            "status": "active",
            "type": {
                "code": "M",
                "display": "Medical"
            },
            "groupNumber": "1111111",
            "grpBillingNumber": "0000",
            "originalEffectiveDate": "2025-08-25",
            "prefixSubscriberID": "ABC123456789",
            "planPrefix": "HHV",
            "dependent": "10",
            "relationship": {
                "code": "10",
                "display": "Dependent"
            },
            "eligibilityRelationship": {
                "code": "45",
                "display": "Dependent Child"
            },
            "coveragePeriod": {
                "start": "2024-08-25",
                "end": "2025-08-25"
            },
            "marketSegmentCode": "Commercial",
            "productLevel": [
                {
                    "lineOfBusiness": {
                        "code": "A1",
                        "display": "Medical"
                    },
                    "planName": {
                        "code": "10017",
                        "display": "LIC"
                    },
                    "productCategory": {
                        "code": "3",
                        "display": "Preferred Provider Plan"
                    },
                    "coveragePackageCode": "123456",
                    "Network": {}
                }
            ],
            "nascoEligibility": {}
        }
    ]
}

ERROR_RESPONSE = {"text": "error, no info found"}

# Accumulator Search Endpoints

# Response data
ACCUM_RESPONSE_SUCC = {
    "member": {
        "subscriberId": "123456789",
        "memberSuffix": "01",
        "firstName": "TEST",
        "lastName": "MEMBER",
        "gender": "female",
        "dateOfBirth": "2089-01-06"
    },
    "planBenefitsAndAccums": [
        {
            "plan": {
                "typeId": "127",
                "marketingName": "TEST",
                "planName": "TEST",
                "type": "TEST",
                "description": "Group, Nongroup"
            },
            "group": {
                "name": "TEST INC.",
                "id": "12345",
                "anniversaryDate": "0101",
                "lob": "A1"
            },
            "benefit": {
                "benefitString": "1234",
                "limitString": "4567",
                "utilizationReviewString": "99999",
                "benefitName": "1234"
            },
            "planLevelBenefitInfo": {
                "benefitMaximums": {
                    "benefitMaximum": [
                        {
                            "nascoAccumId": "12345",
                            "network": "In/Out",
                            "maximumType": "OutOfPocket",
                            "amount": "6450.0",
                            "remainingAmount": "6450.0",
                            "unit": "TEST UNIT",
                            "period": "TEST PERIOD",
                            "provisionalText": "TEST"
                        },
                        {
                            "nascoAccumId": "67890",
                            "network": "In/Out",
                            "maximumType": "OutOfPocket",
                            "remainingAmount": "6450.0",
                            "amount": "123.0",
                            "unit": "TEST UNIT",
                            "period": "TEST PERIOD",
                            "provisionalText": "TEST"
                        }
                    ]
                },
                "memberCost": {
                    "memberCostComponent": [
                        {
                            "nascoAccumId": "123456",
                            "network": "In/Out",
                            "costType": "Deductible",
                            "amount": "123.0",
                            "remainingAmount": "6450.0",
                            "unit": "per individual TEST",
                            "period": "TEST",
                            "provisionalText": "TEST"
                        },
                        {
                            "nascoAccumId": "05105",
                            "network": "In/Out",
                            "costType": "Deductible",
                            "amount": "123.0",
                            "remainingAmount": "6450.0",
                            "unit": "TEST",
                            "period": "per plan TEST",
                            "provisionalText": "TEST"
                        }
                    ]
                }
            }
        }
    ]
}

ACCUM_RESPONSE_REM_AMT_MISS = {
    "member": {
        "subscriberId": "123456789",
        "memberSuffix": "01",
        "firstName": "TEST",
        "lastName": "MEMBER",
        "gender": "female",
        "dateOfBirth": "2089-01-06"
    },
    "planBenefitsAndAccums": [
        {
            "plan": {
                "typeId": "127",
                "marketingName": "TEST",
                "planName": "TEST",
                "type": "TEST",
                "description": "Group, Nongroup"
            },
            "group": {
                "name": "TEST INC.",
                "id": "12345",
                "anniversaryDate": "0101",
                "lob": "A1"
            },
            "benefit": {
                "benefitString": "1234",
                "limitString": "4567",
                "utilizationReviewString": "99999",
                "benefitName": "1234"
            },
            "planLevelBenefitInfo": {
                "benefitMaximums": {
                    "benefitMaximum": [
                        {
                            "nascoAccumId": "12345",
                            "network": "In/Out",
                            "maximumType": "OutOfPocket",
                            "amount": "6450.0",
                            "unit": "TEST UNIT",
                            "period": "TEST PERIOD",
                            "provisionalText": "TEST"
                        },
                        {
                            "nascoAccumId": "67890",
                            "network": "In/Out",
                            "maximumType": "OutOfPocket",
                            "remainingAmount": "6450.0",
                            "amount": "123.0",
                            "unit": "TEST UNIT",
                            "period": "TEST PERIOD",
                            "provisionalText": "TEST"
                        }
                    ]
                },
                "memberCost": {
                    "memberCostComponent": [
                        {
                            "nascoAccumId": "123456",
                            "network": "In/Out",
                            "costType": "Deductible",
                            "amount": "123.0",
                            "unit": "per individual TEST",
                            "period": "TEST",
                            "provisionalText": "TEST"
                        },
                        {
                            "nascoAccumId": "05105",
                            "network": "In/Out",
                            "costType": "Deductible",
                            "amount": "123.0",
                            "remainingAmount": "6450.0",
                            "unit": "TEST",
                            "period": "per plan TEST",
                            "provisionalText": "TEST"
                        }
                    ]
                }
            }
        }
    ]
}

ACCUM_RESPONSE_F = {
    "operationOutcome": {
        "issue": [
            {
                "severity": "warning",
                "code": "00027",
                "details": [
                    {
                        "text": "NASCO error: XXXXX"
                    }
                ],
                "diagnostics": "ReqID - 1234: NASCO error: TEST"
            }
        ]
    },
    "member": {
        "subscriberId": "123456789",
        "memberSuffix": "01",
        "firstName": "TEST",
        "lastName": "MEMBER",
        "gender": "female",
        "dateOfBirth": "2089-01-06"
    },
    "planBenefitsAndAccums": [
        {
            "plan": {
                "typeId": "127",
                "marketingName": "TEST",
                "planName": "TEST",
                "type": "TEST",
                "description": "Group, Nongroup"
            },
            "group": {
                "name": "TEST INC.",
                "id": "12345",
                "anniversaryDate": "0101",
                "lob": "A1"
            },
            "benefit": {
                "benefitString": "1234",
                "limitString": "4567",
                "utilizationReviewString": "99999",
                "benefitName": "1234"
            },
            "planLevelBenefitInfo": {
                "benefitMaximums": {
                    "benefitMaximum": [
                        {
                            "nascoAccumId": "12345",
                            "network": "In/Out",
                            "maximumType": "OutOfPocket",
                            "amount": "6450.0",
                            "unit": "TEST UNIT",
                            "period": "TEST PERIOD",
                            "provisionalText": "TEST"
                        },
                        {
                            "nascoAccumId": "67890",
                            "network": "In/Out",
                            "maximumType": "OutOfPocket",
                            "amount": "123.0",
                            "unit": "TEST UNIT",
                            "period": "TEST PERIOD",
                            "provisionalText": "TEST"
                        }
                    ]
                },
                "memberCost": {
                    "memberCostComponent": [
                        {
                            "nascoAccumId": "123456",
                            "network": "In/Out",
                            "costType": "Deductible",
                            "amount": "123.0",
                            "unit": "per individual TEST",
                            "period": "TEST",
                            "provisionalText": "TEST"
                        },
                        {
                            "nascoAccumId": "05105",
                            "network": "In/Out",
                            "costType": "Deductible",
                            "amount": "123.0",
                            "unit": "TEST",
                            "period": "per plan TEST",
                            "provisionalText": "TEST"
                        }
                    ]
                }
            }
        }
    ]
}

# Accumulator Endpoints
@app.get("/searchAccums/acc-succ", response_model=AccumulatorResponse)
async def search_accum_success():
    """Search for accumulator with ID 'acc-succ'"""
    return ACCUM_RESPONSE_SUCC

@app.get("/searchAccums/acc-rem-amt-miss", response_model=AccumulatorResponse)
async def search_accum_rem_amt_miss():
    """Search for accumulator with ID 'acc-rem-amt-miss'"""
    return ACCUM_RESPONSE_REM_AMT_MISS

@app.get("/searchAccums/acc-f", response_model=FailedAccumulatorResponse)
async def search_accum_failure():
    """Search for accumulator with ID 'acc-f'"""
    return ACCUM_RESPONSE_F

# Coverage Search Endpoints
@app.get("/searchCoverageById/c-s", response_model=CoverageResponse)
async def search_coverage_cs():
    """Search for coverage with ID 'c-s'"""
    return COVERAGE_RESPONSE_CS

@app.get("/searchCoverageById/c-n-m-id", response_model=CoverageResponse)
async def search_coverage_cnmid():
    """Search for coverage with ID 'c-n-m-id'"""
    return COVERAGE_RESPONSE_CNMID

@app.get("/searchCoverageById/c-n-a-c", response_model=CoverageResponse)
async def search_coverage_cnac():
    """Search for coverage with ID 'c-n-a-c'"""
    return COVERAGE_RESPONSE_CNAC

@app.get("/searchCoverageById/c-e-r", response_model=ErrorResponse)
async def search_coverage_error():
    """Return error for coverage search"""
    return ERROR_RESPONSE

@app.get("/searchMemberById/m-a", response_model=MemberResponse)
async def search_member_ma():
    """Search for member with ID 'm-a'"""
    return MEMBER_RESPONSE_MA

@app.get("/searchMemberById/m-b-m-n", response_model=MemberResponse)
async def search_member_m_b_m_n():
    """Search for member with ID 'm-b-m-n'"""
    return MEMBER_RESPONSE_MBMN

@app.get("/searchMemberById/m-n-a-c", response_model=MemberResponse)
async def search_member_m_n_a_c():
    """Search for member with ID 'm-n-a-c'"""
    return MEMBER_RESPONSE_MNAC

@app.get("/searchMemberById/m-e-r", response_model=ErrorResponse)
async def search_member_error():
    """Return error for member search"""
    return ERROR_RESPONSE

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        workers=1 if os.getenv("ENV") == "development" else None
    )
