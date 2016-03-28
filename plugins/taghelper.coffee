
module.exports = (env, callback) ->
  getNumTags = (tag) ->
    tags = env.helpers.getAllTags()
    numTags = tags.filter (thisTag) -> tag == thisTag
    return numTags.length

  # add the article helper to the environment so we can use it later
  env.helpers.getNumTags = getNumTags

  # tell the plugin manager we are done
  callback()
