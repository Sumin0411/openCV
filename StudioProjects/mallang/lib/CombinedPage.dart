import 'package:flutter/material.dart';
import 'package:mallang/main.dart';

class TermsOfService extends StatefulWidget {
  const TermsOfService({Key? key}) : super(key: key);

  @override
  State<TermsOfService> createState() => _TermsOfServiceState();
}

class _TermsOfServiceState extends State<TermsOfService> {
  int index = 0;

  Widget _topMenu() {
    return Wrap(
      children: [
        _menuOne(
          menu: '서비스 이용약관 동의(필수)',
          isActive: index == 0,
          onTap: () {
            index = 0;
            update();
          },
        ),
        _menuOne(
            menu: '개인정보 수집 및 이용동의(필수)',
            isActive: index == 1,
            onTap: () {
              index = 1;
              update();
            }),
        _menuOne(
            menu: '품질 향상을 위한 이용자 데이터 수집(선택)',
            isActive: index == 2,
            onTap: () {
              index = 2;
              update();
            }),
        _menuOne(
            menu: '마케팅 정보 수신 동의(선택)',
            isActive: index == 3,
            onTap: () {
              index = 3;
              update();
            }),
        _menuOne(
            menu: '마케팅 정보 수신 동의(선택)',
            isActive: index == 4,
            onTap: () {
              index = 3;
              update();
            }),
      ],
    );
  }

  void update() => setState(() {});

  Widget _menuOne(
      {required String menu,
        required bool isActive,
        required Function() onTap}) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        width: MediaQuery.of(context).size.width,
        height: 50,
        decoration: BoxDecoration(
          border: Border.all(
              width: 1,
              color:
              isActive ? const Color(0xffe53154) : const Color(0xffcccccc)),
          color: const Color(0xfffafafa),
        ),
        child: Center(
          child: Text(
            menu,
            style: TextStyle(
              color: isActive ? const Color(0xffe53154) : Colors.black,
              fontWeight: isActive ? FontWeight.bold : FontWeight.normal,
            ),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        centerTitle: true,
        title: const Text('말랑 서비스 약관 동의'),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Padding(padding: const EdgeInsets.all(10), child: _topMenu()),
          ],
        ),
      ),
    );
  }
}