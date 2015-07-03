
import ckan.plugins as p
import ckanext.stcndm.logic.common as common
import ckanext.stcndm.logic.cubes as cubes

class STCNDMPlugin(p.SingletonPlugin):
    p.implements(p.IActions)
    p.implements(p.IConfigurer)
    p.implements(p.IPackageController, inherit=True)

    def update_config(self, config):
        """
        Add configuration we need during startup
        """
        p.toolkit.add_template_directory(config, "templates")
        #p.toolkit.add_public_directory(config, "static")

    def before_index(self, data_dict):
        """
        customize data sent to solr
        """
        return data_dict

    def get_actions(self):
        return {
            "ndm_get_cube": cubes.get_cube,
            "GetProduct": common.get_product
        }
