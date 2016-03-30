
module.exports = (env, callback) ->
  shuffle = (a) ->
    for i in [a.length-1..1]
      j = Math.floor Math.random() * (i + 1)
      [a[i], a[j]] = [a[j], a[i]]
    a

  # add the article helper to the environment so we can use it later
  env.helpers.shuffle = shuffle

  # tell the plugin manager we are done
  callback()
