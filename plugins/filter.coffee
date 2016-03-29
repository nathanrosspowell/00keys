
module.exports = (env, callback) ->
  passesTagFilter = (page, filters) ->
    keypageTags = env.helpers.getTagsFromArticle(page)
    for filter in filters
        if keypageTags.indexOf(filter) == -1
            return false
    return true

  # add the article helper to the environment so we can use it later
  env.helpers.passesTagFilter = passesTagFilter

  # tell the plugin manager we are done
  callback()
