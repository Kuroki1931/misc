import sonnet as snt
import graph_nets as gn
import tensorflow as tf

def get_graphs():
    data_dict = dict(
        nodes=[[2.], [3.], [0.]], 
        receivers=[2, 2],
        senders=[0, 1],
        n_node=3,
        n_edge=2,
    )
    return gn.utils_tf.data_dicts_to_graphs_tuple([data_dict]) 

graph_net_module = gn.modules.GraphIndependent(
    node_model_fn=lambda: snt.nets.MLP([8, 1]),
)

input_graphs = get_graphs()
input_graph_tr = gn.utils_tf.make_runnable_in_session(input_graphs) 

output_graphs = graph_net_module(input_graph_tr)  

loss_op_tr = tf.reduce_sum((output_graphs.nodes[2] - 5) ** 2)  # reduce_sum 要らないかも

learning_rate = 1e-2
optimizer = tf.train.AdamOptimizer(learning_rate)
step_op = optimizer.minimize(loss_op_tr)

# Init Session
try:
  sess.close()
except NameError:
  pass
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Run Training

loss_history = []
for _ in range(1000):
    train_values = sess.run({
      "loss": loss_op_tr,
      "step": step_op,
      "outputs": output_graphs 
    })
    loss_history.append(train_values['loss'])

print(train_values)
print(train_values['outputs'].nodes[2])