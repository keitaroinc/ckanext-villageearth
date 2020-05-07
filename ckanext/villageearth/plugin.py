import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import helpers as h


class VillageearthPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'villageearth')

    def get_helpers(self):
        '''Register all custom template
        helper functions.
        '''
        return {'get_most_popular_groups': h.most_popular_groups}