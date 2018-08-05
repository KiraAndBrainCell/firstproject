print "reached module actions"
from libs.product import module_actions
import axon.api.supervisor as api

if __name__ == "__main__":
    # omc_authenticate
    if api.get_action() == "omc_rest_auth_action":
        print "first action"
        ApplianceIP = api.get_input_value("ApplianceIP")
        print "Appliance IP is %s" % ApplianceIP
        user_name = api.get_input_value("user_name")
        password = api.get_input_value("password")
        port = api.get_input_value("port")
        flag, msg, sessionID = module_actions.omc_rest_auth_action(ApplianceIP, user_name, password, port=port)
        resultJson = {"flag" : flag, "msg" : msg, "sessionID" : sessionID}
        print "Result.json is %s" % resultJson
        api.setall_output_values(resultJson)

    elif api.get_action() == "omc_con_Prof_action":
        #omc_con_Prof_action
        ApplianceIP = api.get_input_value("ApplianceIP")
        sessionID = api.get_input_value("sessionID")
        port = api.get_input_value("port")
        flag, msg, conProfID = module_actions.omc_con_Prof_action(ApplianceIP, sessionID, port=port)
        resultJson = {"flag" : flag, "msg" : msg, "conProfID" : conProfID}
        print "Result.json is %s" % resultJson
        api.setall_output_values(resultJson)

    elif api.get_action() == "omc_create_disc_action":
        # omc_create_disc_action
        ApplianceIP = api.get_input_value("ApplianceIP")
        sessionID = api.get_input_value("sessionID")
        port = api.get_input_value("port")
        iprange = api.get_input_value("iprange")
        con_prof_id = api.get_input_value("con_prof_id")
        flag, msg, dis_taskID = module_actions.omc_create_disc_action(ApplianceIP, 
                                              sessionID, iprange, con_prof_id, port=port)
        resultJson = {"flag" : flag, "msg" : msg, "dis_taskID" : dis_taskID}
        print "Result.json is %s" % resultJson
        api.setall_output_values(resultJson)
        