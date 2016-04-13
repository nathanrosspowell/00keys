
module.exports = (env, callback) ->

  passesTagFilter = (page, filters) ->
    if not filters 
      return 'filters are fucked'
    if not filters.length 
      return 'filters isnt an array'
    keypageTags = env.helpers.getTagsFromArticle(page)
    if not keypageTags 
      reutn 'keypages are fucked'
    if not keypageTags.length
      return 'keypageTags isnt an array'
    if keypageTags.indexOf("Canceled") != -1
      return 'canceled'
    for filter in filters
      if keypageTags.indexOf(filter) == -1
        return 'not in index'
    return true

  getFilteredKeys = (contents, tag, filters) ->
    passes = []
    for keypage in env.helpers.sortById(env.helpers.getArticlesByTag(contents, tag)) 
      if passesTagFilter(keypage, filters) is true
        passes.push keypage
    return passes

  # add the article helper to the environment so we can use it later
  env.helpers.passesTagFilter = passesTagFilter
  env.helpers.getFilteredKeys = getFilteredKeys

  # tell the plugin manager we are done
  callback()
