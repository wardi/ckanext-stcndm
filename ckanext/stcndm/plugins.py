
import ckan.plugins as p
import ckanext.stcndm.logic.codesets as codesets
import ckanext.stcndm.logic.common as common
import ckanext.stcndm.logic.cubes as cubes
import ckanext.stcndm.logic.daily as daily
import ckanext.stcndm.logic.publications as pubs
import ckanext.stcndm.logic.subjects as subjects
import ckanext.stcndm.logic.views as views

from ckanext.stcndm import validators

class STCNDMPlugin(p.SingletonPlugin):
    p.implements(p.IActions)
    p.implements(p.IConfigurer)
    p.implements(p.IPackageController, inherit=True)
    p.implements(p.IValidators)

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
        # Some Java web clients require the web service to use Pascal Case
        return {
            "DeleteProduct": common.delete_product,
            "GetBookableReleases": daily.get_bookable_releases,
            "GetCubeList": cubes.get_cube_list_by_subject,
            "GetDefaultViews": daily.get_default_views,
            "GetDerivedProductList": common.get_derived_product_list,
            "GetProduct": common.get_product,
            "GetProductIssueArticles": daily.get_product_issue_articles,
            "GetProductIssues": daily.get_product_issues,
            "GetProductType": common.get_product_type,
            "GetSubjectList": subjects.get_top_level_subject_list,
            "GetSurveys": daily.get_surveys,
            "GetThemes": daily.get_themes,
            "GetUpcomingReleases": common.get_upcoming_releases,
            "PurgeDataset": common.purge_dataset,
            "RegisterCube": cubes.register_cube,
            "RegisterProduct": common.tv_register_product,
            "UpdateProductGeo": common.update_product_geo,
            "UpdatePublishingStatus": common.get_last_publish_status,
        }

    def get_validators(self):
        return {
            "shortcode_validate": validators.shortcode_validate,
            "shortcode_output": validators.shortcode_output,
        }

