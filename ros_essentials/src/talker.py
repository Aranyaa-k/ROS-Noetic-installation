import rospy 
from std_msgs.msg import String

def talker():
    pub=rospy.Publisher('chatter',String,queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(1)

    i=1
    while not rospy.is_shutdown():
        s="Bye World %s" % i
        #rospy.loginfo(s)
        print(s)
        pub.publish(s)
        rate.sleep()
        i+=1


if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
        
     
