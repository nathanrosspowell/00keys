
module.exports = (env, callback) ->
  sortById = (articles) ->
    articles.sort (a, b) -> parseInt b.metadata.id - parseInt a.metadata.id
    return articles

  # add the article helper to the environment so we can use it later
  env.helpers.sortById = sortById

  # tell the plugin manager we are done
  callback()
