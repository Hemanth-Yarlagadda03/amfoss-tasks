import 'package:flutter/material.dart';
import 'package:onboarding_screen_example/main.dart';
import 'package:onboarding_screen_example/page/onboarding_page.dart';
import 'package:onboarding_screen_example/widget/button_widget.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(
          title: Text(MyApp.title),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.asset('assets/welcome.png'), 
              Text(
                'Hemanth Lakshman Yarlagadda',
                style: TextStyle(fontSize: 45, fontWeight: FontWeight.bold),
                
              ),
              Text(
                'I am a sports,science,leterature,history and an animal lover from Hyderabad,Telangana:)',
              

                textAlign: TextAlign.center,
               //softWrap: true,
               style: TextStyle(
               color: Colors.blue[900],
               fontSize: 20,)
              ),
              //Text('df'),
            ],
          ),
        ),
      );

  void goToOnBoarding(context) => Navigator.of(context).pushReplacement(
        MaterialPageRoute(builder: (_) => OnBoardingPage()),
      );
}
