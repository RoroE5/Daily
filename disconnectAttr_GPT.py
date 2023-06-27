import maya.cmds as cmds

# 获取与节点 A 相连接的所有连接，并断开它们
def disconnect_all_connections(node_a):
    connections = cmds.listConnections(node_a, source=True, destination=True, plugs=True)
    if connections:
        for connection in connections:
            cmds.disconnectAttr(connection, node_a)

# 示例使用
node_a = 'nodeA.attribute'  # 要断开连接的节点 A 和属性

# 断开所有连接
disconnect_all_connections(node_a)
