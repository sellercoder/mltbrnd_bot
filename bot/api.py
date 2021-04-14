from utils.models import *


def getProviders():
    providers = Provider.all()
    return providers

def getProvider(provider_id):
    provider = Provider.find(provider_id)
    return provider

def addPlan(provider_id,name,description,price):
    plan = Plan()
    plan.provider_id = provider_id
    plan.name = name
    plan.description = description
    plan.price = price
    plan.save()
    return plan











