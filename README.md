# pip-inventory
New Relic Infrastructure Integration for reporting python modules

1. Deploy according to location descriptions here: https://docs.newrelic.com/docs/integrations/integrations-sdk/getting-started/integration-file-structure-activation

2. Modify pip-list-definition.yml to include the name of the user you wish to run as

3. OPTIONAL - If desired, modify runpip.sh to use python3. Or, if running both python2 and python3, create two versions and give two definitions in pip-list-definition.yml to run each for a different prefix
