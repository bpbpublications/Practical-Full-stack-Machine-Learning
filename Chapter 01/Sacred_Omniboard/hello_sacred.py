# from sacred import Experiment

# ex = Experiment()

# @ex.config
# def my_config():
#     recipient = "Sacred"
#     message = "Hello %s!" % recipient


# @ex.automain
# def my_main(message):
#     print(message)

# # if __name__ == '__main__':
# #     ex.run_commandline()

# from sacred import Experiment

# ex = Experiment()

# @ex.config
# def my_config(): 
#     x = 5 #some integer --2
#     conf = {'foo': '10', 'bar':'ten'}

# @ex.main
# def my_main(x, conf): 
#     print(f"x = {x}")
#     print(f"foo = {conf['foo']}")

# ex.run()

from sacred import Experiment

ex = Experiment()

ex.add_config({
  'foo': 12,
  'bar': 'twelve'
})

@ex.main
def my_main(foo, bar):
    print(f"foo = {foo}")
    print(f"bar = {bar}")
ex.run()
