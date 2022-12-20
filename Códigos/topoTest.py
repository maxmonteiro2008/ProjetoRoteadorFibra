from mininet.topo import Topo

class MyTopo( Topo ):

	def __init__( self ):

		Topo.__init__( self )
		 
		h1 = self.addHost( 'h1' )

		h2 = self.addHost( 'h2' )

		h3 = self.addHost( 'h3' )


		s1 = self.addSwitch( 's1' )

		s2 = self.addSwitch( 's2' )

		s3 = self.addSwitch( 's3' )

		s4 = self.addSwitch( 's4' )

		s5 = self.addSwitch( 's5' )


		#Adicionando links


		self.addLink(h1,s1,bw=100,delay='5ms',loss=1,max_queue_size=10000,use_htb=True)

		self.addLink(h2,s1,bw=100,delay='5ms',loss=1,max_queue_size=10000,use_htb=True)

		self.addLink(h3,s5,bw=100,delay='5ms',loss=1,max_queue_size=10000,use_htb=True)
		 

		self.addLink(s1,s2,bw=100,delay='5ms',loss=1,max_queue_size=10000,use_htb=True)

		self.addLink(s1,s3,bw=100,delay='5ms',loss=1,max_queue_size=10000,use_htb=True)

		self.addLink(s1,s4,bw=100,delay='5ms',loss=1,max_queue_size=10000,use_htb=True)

		self.addLink(s2,s5,bw=100,delay='5ms',loss=1,max_queue_size=10000,use_htb=True)

		self.addLink(s3,s5,bw=100,delay='5ms',loss=1,max_queue_size=10000,use_htb=True)

		self.addLink(s4,s5,bw=100,delay='5ms',loss=1,max_queue_size=10000,use_htb=True)


topos = { 'mytopo': ( lambda: MyTopo() ) }