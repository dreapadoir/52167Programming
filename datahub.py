from datapackage import Package

package = Package('https://datahub.io/machine-learning/iris/datapackage.json')

# print list of all resources:
print(package.resource_names)

